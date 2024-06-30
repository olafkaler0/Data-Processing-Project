# fetcher.py

import requests
from logger import setup_logger

logger = setup_logger('fetcher')

def fetch_data(api_url, username, password):
    logger.info("Fetching data from API.")
    try:
        response = requests.get(api_url, auth=(username, password))
        if response.status_code == 200:
            logger.info("Data fetched successfully.")
            return response.json()
        else:
            logger.error(f"Failed to fetch data: {response.status_code}")
            return None
    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        return None
