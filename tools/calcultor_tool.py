from core.logger import logger


def calculate(expression):

    logger.info("=" * 50)
    logger.info(f"Calculating tool called with expression: {expression}")

    try:
        logger.info("Evaluating expression using eval()")

        result = eval(expression)

        logger.info(f"Calculation result: {result}")
        logger.info("Calculation completed successfully")
        logger.info("=" * 50)

        return f"Answer: {result}"

    except Exception as e:

        logger.error(f"Error in calculation: {str(e)}")
        logger.info("=" * 50)

        return str(e)