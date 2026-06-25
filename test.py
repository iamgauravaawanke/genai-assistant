import uvicorn
from tools.weather_tool import get_weather
from tools.news_tool import get_news
from tools.search_tool import search_web
from tools.calcultor_tool import calculate
from tools.travel_tool import get_travel_info
from models.llm import ask_qwen
from models.embedding import embedding
from core.logger import logger
from core.memory import load_memory, save_memory
from fastapi import FastAPI , UploadFile , File , HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from core.database import get_db_connection
import pathlib
import os
from PyPDF2 import PdfReader
from rag.chunking import chunks_split
import chromadb


app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
client = chromadb.PersistentClient(
    path="./chroma_db"
)

# # Create a collection (equivalent to a table in SQL)
collection = client.get_or_create_collection(
    name="chat_collection"
)




class ChatRequest(BaseModel):
    message: str
    session_id: int


def run_agent(user_input):

    logger.info("=" * 50)
    logger.info(f"Agent received input: {user_input}")

    lower_input = user_input.lower() 

    if "weather" in lower_input:
        city = lower_input.replace("weather", "").strip()
        return get_weather(city)

    elif "news" in lower_input:
        topic = lower_input.replace("news", "").strip()
        return get_news(topic)

    elif "calculate" in lower_input:
        expression = lower_input.replace("calculate", "").strip()
        return calculate(expression)

    elif "travel" in lower_input:
        place = lower_input.replace("travel", "").strip()
        return get_travel_info(place)

    else:
        return "No tool needed."

@app.post("/chat")
def chat_endpoint(data: ChatRequest):
    
 
    
    

    logger.info("=" * 50)
    logger.info("CHAT REQUEST STARTED")

    user_input = data.message
    lower_input = user_input.lower()

    logger.info(f"Received user input: {user_input}")

    memory = load_memory()

    logger.info("Memory loaded successfully")

    try:

        # =========================
        # RECENT HISTORY
        # =========================

        logger.info("Fetching recent chat history")

        recent_history = memory["chat_history"][-5:]

        logger.info(
            f"Recent history count: {len(recent_history)}"
        )

        context = ""

        logger.info("Building conversation context")

        for chat in recent_history:

            context += f"""
            User: {chat['user_input']}
            Bot: {chat['response']}
            """

        logger.info("Context built successfully")

        # =========================
        # MEMORY UPDATE
        # =========================

        logger.info("Updating memory")

        if "i am " in lower_input:

            name = user_input[5:].strip()

            memory["user_profile"]["name"] = name

            logger.info(
                f"Updated user name memory: {name}"
            )

        if "i like " in lower_input:

            interest = (
                user_input.split("i like ")[-1]
                .replace("?", "")
                .strip()
            )

            memory["user_profile"]["interest"] = interest

            logger.info(
                f"Updated interest memory: {interest}"
            )

        if "weather in " in lower_input:

            city = (
                user_input.split("weather in ")[-1]
                .strip()
            )

            memory["user_profile"]["last_city"] = city

            logger.info(
                f"Updated last city memory: {city}"
            )

        # =========================
        # MEMORY QUESTIONS
        # =========================

        logger.info("Checking memory questions")

        if "what is my name" in lower_input:

            response = (
                f"Your name is "
                f"{memory['user_profile']['name']}"
            )

            logger.info(
                "Answered from memory: name"
            )

        elif "what do i like" in lower_input:

            response = (
                f"You like "
                f"{memory['user_profile']['interest']}"
            )

            logger.info(
                "Answered from memory: interest"
            )

        else:

            # =========================
            # TOOL CALLING
            # =========================

            logger.info(
                "Processing request through agent"
            )

            tool_result = run_agent(user_input)

            logger.info(
                f"Tool result: {tool_result}"
            )
            
            
            logger.info("=" * 50)
            logger.info("RAG RETRIEVAL STARTED")
            logger.info("Generating Question Embedding")
           
            question_vector = embedding(user_input)
            logger.info(
            f"Question Embedding Generated Successfully")
            
            logger.info("Searching ChromaDB")
            
            question_searching = collection.query(
                query_embeddings=[question_vector],
                n_results=5,
                include=["documents", "distances"]
                )

            logger.info(
            f"Distances: {question_searching['distances'][0]}")
            print(question_searching["documents"])
            print(question_searching["distances"])

            logger.info("ChromaDB Search Completed")
            # Build Context
            logger.info("Building RAG Context")
            reterival_chunks = question_searching['documents'][0]
            
            if len(reterival_chunks) == 0:
                logger.info("No RAG chunks found. Using normal LLM.")

                response = ask_qwen(user_input)

            else:
                
            # print(reterival_chunks)
                rag_context = "\n".join(reterival_chunks)
                # print(rag_context)
                logger.info(f"Retrieved {len(reterival_chunks)} chunks")
                logger.info("RAG Context Preview:")
        
                logger.info("RAG RETRIEVAL COMPLETED")
                
                
                # =========================
                # FINAL PROMPT
                # =========================
                logger.info("Preparing final prompt")
                final_prompt = f"""
                    You are a RAG assistant.

                    Previous Conversation:
                    {context}

                    Retrieved Context:
                    {rag_context}

                    Tool Result:
                    {tool_result}

                    Current User Query:
                    {user_input}

                    Rules:
                    1. Answer ONLY using information from the Retrieved Context.
                    2. Do NOT use your own knowledge.
                    3. Do NOT make assumptions.
                    4. If the answer is not explicitly present in the Retrieved Context, respond exactly with:

                    I could not find that information in the uploaded documents.

                    5. Keep the answer concise.

                    Answer:
                    """

                logger.info("Sending final prompt to LLM")
                response = ask_qwen(final_prompt)
            logger.info(f"LLM response generated: {response}")
            logger.info("Connecting to PostgreSQL")
            conn = get_db_connection()
            logger.info("PostgreSQL connection successful")
            session_id = data.session_id 
            logger.info(f"Session ID Received: {session_id}")
            cursor = conn.cursor()
            logger.info("Cursor created")
            logger.info("Cursor created")
            # Save message first
            cursor.execute(
                """
                INSERT INTO messages
                (session_id, user_input, ai_response)
                VALUES (%s, %s, %s)
                """,
                (session_id, user_input, response)
            )
            logger.info("Message inserted")
            # Check current session title
            cursor.execute(
                """
                SELECT title
                FROM sessions
                WHERE session_id = %s
                """,
                (session_id,)
            )
            row = cursor.fetchone()
            logger.info(f"Session Query Result: {row}")
            
            
            if row is None:
                logger.error(
                f"No session found for session_id={session_id}")
            else:
                title = row[0]
                
            # If title is empty, create title from first message
                if title == "":
                    title = " ".join(user_input.split()[:4])

                    cursor.execute(
                    """
                    UPDATE sessions
                    SET title = %s
                    WHERE session_id = %s
                    """,
                    (title, session_id)
                    )

                    logger.info(f"Session title updated: {title}")
                    logger.error(f"No session found for session_id={session_id}")
            conn.commit()
            logger.info("Transaction committed")
            logger.info("INSERT successful")
            conn.commit()
            cursor.close()
            logger.info("Cursor closed")
            conn.close()
            logger.info("Database connection closed")
        # =========================
        # SAVE CHAT HISTORY
        # =========================
        logger.info("Saving chat history")
        memory["chat_history"].append({
            "user_input": user_input,
            "response": response
        })
        # =========================
        # SAVE MEMORY
        # =========================
        logger.info("Saving memory to file")
        save_memory(memory)
        logger.info(
            "Memory saved successfully"
        )
        logger.info("CHAT REQUEST COMPLETED")
        logger.info("=" * 50)
        return {
            "response": response
        }
    except Exception as e:
        logger.error(
            f"Error occurred: {str(e)}"
        )
        return {
            "error": str(e)
        }
        
@app.get("/messages/{session_id}")
def get_messages(session_id: int):

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT
            id,
            user_input,
            ai_response,
            session_id
        FROM messages
        WHERE session_id = %s
        ORDER BY id ASC
        """,
        (session_id,)
    )

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    data = []

    for row in rows:

        data.append({
            "id": row[0],
            "user_input": row[1],
            "ai_response": row[2],
            "session_id": row[3]
        })

    return data


@app.get("/get_all_sessions")
def get_all_sessions():

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT session_id, title
        FROM sessions
        ORDER BY session_id DESC
        """
    )

    rows = cursor.fetchall()
    # logger.info(f"Rows: {rows}")

    cursor.close()
    conn.close()

    sessions = []

    for row in rows:

        sessions.append({
            "session_id": row[0],
            "title": row[1]
        })

    return sessions



@app.post("/sessions")
def create_session():

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO sessions(title)
        VALUES ('')
        RETURNING session_id
        """
    )

    session_id = cursor.fetchone()[0]

    conn.commit()

    cursor.close()
    conn.close()

    return {
        "session_id": session_id
    }
    
    
#====================RAG================
directory = r"C:\Users\gaura\OneDrive\Documents\ai-agent\upload"

@app.post("/upload_file")
async def upload_file(file: UploadFile = File(...)):
    try:
        logger.info(f"Received file: {file.filename}")

        filepath = os.path.join(directory, file.filename)

        content = await file.read()

        with open(filepath, "wb") as f:
            f.write(content)

        logger.info(f"File saved successfully: {filepath}")

        reader = PdfReader(filepath)

        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""

        logger.info(f"Extracted text length: {len(text)}")

        real_chunks = chunks_split(text)
        logger.info(f"Total chunks created: {len(real_chunks)}")

        for i, chunk in enumerate(real_chunks):

            embedding_vector = embedding(chunk)
            # print(type(embedding_vector))

            collection.add(
    ids=[f"{file.filename}_{i}"],
    documents=[chunk],
    embeddings=[embedding_vector],
    metadatas=[{
        "source": file.filename,
        "chunk_id": i
    }]
)
            # logger.info(f"Chunk stored in vector DB: {i}")
            # logger.info(f"Stored Chunk {i+1}/{len(cs)}")

        logger.info(f"Completed processing file: {file.filename}")

        return {
            "message": "PdF stored in vector database successfully",
            "chunks": len(real_chunks)
        }

    except Exception as e:

        logger.exception(f"Error processing file: {file.filename}")

        raise HTTPException(
            status_code=500,
            detail=f"An error occurred: {str(e)}"
        )
        
    
            

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)