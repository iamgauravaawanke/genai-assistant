import requests
from config.settings import SEARCH_API_KEY
from core.logger import logger


def search_web(query):

    logger.info("=" * 50)
    logger.info("Search tool execution started")
    logger.info(f"Search tool called with query: {query}")

    url = "https://google.serper.dev/search"

    logger.info("Search API URL created successfully")

    payload = {"q": query}

    logger.info(f"Payload created: {payload}")

    headers = {
        "X-API-KEY": SEARCH_API_KEY,
        "Content-Type": "application/json"
    }

    logger.info("Headers created successfully")

    response = requests.post(url, json=payload, headers=headers)

    logger.info(f"API Response Status Code: {response.status_code}")

    data = response.json()

    logger.info("API response converted to JSON")

    results = data["organic"][:3]

    logger.info(f"Top {len(results)} search results extracted")

    output = []

    for item in results:
        output.append(item["title"])

    logger.info(f"Search tool result: {output}")
    logger.info("Returning search results to user")
    logger.info("=" * 50)

    return "\n".join(output)