import requests
def embedding(text):
    url = "http://127.0.0.1:1234/v1/embeddings"

    payload = {
        "model": "text-embedding-nomic-embed-text-v1.5",
        "input": text
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()

    result = response.json()

    return result["data"][0]["embedding"]