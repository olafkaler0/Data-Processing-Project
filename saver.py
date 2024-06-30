# saver.py

import json
from logger import setup_logger

logger = setup_logger('saver')

def save_data(file_path, data):
    logger.info("Saving data to file.")
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file)
        logger.info("Data saved successfully.")
    except Exception as e:
        logger.error(f"Error occurred while saving data: {str(e)}")
