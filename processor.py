# processor.py

from logger import setup_logger

logger = setup_logger('processor')

def process_data(data):
    logger.info("Processing data.")
    if data:
        # Simulate processing
        processed_data = data  # This would be where actual processing occurs
        logger.info("Data processed successfully.")
        return processed_data
    else:
        logger.warning("No data to process.")
        return None
