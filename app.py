from tools.weather_tool import get_weather
from tools.news_tool import get_news
from tools.search_tool import search_web
from tools.calcultor_tool import calculate
from tools.travel_tool import get_travel_info
from models.llm import ask_qwen
from core.logger import logger
from core.memory import load_memory, save_memory


def run_agent(user_input):

    logger.info("=" * 50)
    logger.info(f"Agent received input: {user_input}")

    user_input = user_input.lower()

    if "weather" in user_input:
        logger.info("Routing to Weather Tool")
        city = user_input.replace("weather", "").strip()
        return get_weather(city)

    elif "news" in user_input:
        logger.info("Routing to News Tool")
        topic = user_input.replace("news", "").strip()
        return get_news(topic)

    elif "calculate" in user_input:
        logger.info("Routing to Calculator Tool")
        expression = user_input.replace("calculate", "").strip()
        return calculate(expression)

    elif "travel" in user_input:
        logger.info("Routing to Travel Tool")
        place = user_input.replace("travel", "").strip()
        return get_travel_info(place)

    else:
        logger.info("Routing to Search Tool (default)")
        return search_web(user_input)


def start():

    logger.info("=" * 50)
    logger.info("AI Agent started. Type 'exit' to quit.")
    logger.info("=" * 50)

    memory = load_memory()   # ✅ moved inside start

    while True:

        query = input("You: ")
        logger.info(f"User query received: {query}")

        if query == "exit":
            logger.info("Exit command received. Shutting down agent.")
            logger.info("Saving memory before shutdown")    


            save_memory(memory)
            logger.info("Memory saved successfully")
            logger.info("AI Agent stopped")


            break

        try:

            logger.info("Fetching recent chat history")
            recent_history = memory["chat_history"][-2:]

            logger.info(

    
                f"Recent history count: {len(recent_history)}"
            )

            context = ""

            logger.info("Building context for LLM")
            
            for chat in recent_history:
                context +=f"""
                User:{chat["query"]}
                Bot:{chat['response']}
              """

            logger.info("Context built successfully, sending to LLM")


            final_prompt = f"""
            Previous Conversation:
            {context}

            Current User Query:
            {query}

            Answer naturally and shortly.
            """
            logger.info("Final prompt prepared for LLM")
            logger.info("Sending prompt to LLM")





            response = ask_qwen(final_prompt)

            #response = run_agent(query)

            logger.info(f"AI Response generated: {response}")

            print("\nAI:", response)

            logger.info("Saving chat history into memory")







            # memory store
            memory["chat_history"].append({
                "query": query,
                "response": response
            })

            memory["chat_history"].append(...)

            logger.info("Updating user profile memory")

            # safe parsing
            if "i am " in query:
                memory["user_profile"]["name"] = query.split("i am ")[-1].strip()

            if "i like " in query:
                memory["user_profile"]["interest"] = query.split("i like ")[-1].strip()

            if "weather in " in query:
                memory["user_profile"]["last_city"] = query.split("weather in ")[-1].strip()
             


            logger.info("Saving memory to disk")
 
            save_memory(memory)



            logger.info("Memory saved successfully")
            logger.info("=" * 50)

            
            


            




        except Exception as e:

            logger.error(f"Error occurred in agent loop: {str(e)}")
            print("Something went wrong")