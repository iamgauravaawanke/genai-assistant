import requests
from config.settings import NEWS_API_KEY
from core.logger import logger


def get_news(topic):

    logger.info(f"news tool called with topic: {topic}")

    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={NEWS_API_KEY}"

    response = requests.get(url)

    logger.info(f"News API response status code: {response.status_code}")

    data = response.json()

    articles = data["articles"][:5]

    result = []

    for article in articles:
        result.append(article["title"])

    logger.info(f"News tool result: {result}")

    return "\n".join(result)