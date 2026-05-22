from core.logger import logger


def get_travel_info(place):

    logger.info("=" * 50)
    logger.info("Travel tool execution started")
    logger.info(f"Travel Tool called with place: {place}")

    logger.info(f"Generating travel information for: {place}")

    result = f"""
Travel Information for {place}

- Famous Places
- Hotels
- Local Food
- Best Time to Visit
"""

    logger.info(f"Travel information for {place} generated successfully.")
    logger.info("Returning travel information to user")
    logger.info("=" * 50)

    return result