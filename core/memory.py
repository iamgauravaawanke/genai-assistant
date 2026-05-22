import json
import os


MEMORY_FILE = "memory/memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {
            "user_profile": {
                 "name": "",
                "interest": "",
                "last_city": ""

            },
            "chat_historty":[]
        }
    with open(MEMORY_FILE,"r") as f:
        return json.load(f)
    


def save_memory(memory):

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)    
    
    




        