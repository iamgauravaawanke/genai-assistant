import psycopg2

def get_db_connection():

    conn = psycopg2.connect(
        host="localhost",
        database="genai_chatbot",
        user="postgres",
        password="Gaurav@1234",
        port="5432"
    )

    return conn



# conn = get_db_connection()
# print("Connected")