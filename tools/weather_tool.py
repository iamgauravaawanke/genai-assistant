import requests
from config.settings import WEATHER_API_KEY
from core.logger import logger


def get_weather(city):

    logger.info("=" * 50)
    logger.info("Weather tool execution started")
    logger.info(f"Weather tool called with city: {city}")

    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}"

    logger.info("Weather API URL created successfully")

    response = requests.get(url)

    logger.info(f"API Response Status Code: {response.status_code}")

    data = response.json()

    logger.info("API response converted to JSON")

    temp = data["current"]["temp_c"]

    logger.info(f"Extracted temperature for {city}: {temp}°C")

    logger.info(f"Weather information for {city} generated successfully.")
    logger.info("Returning weather result to user")
    logger.info("=" * 50)

    return f"{city} temperature is {temp}°C"