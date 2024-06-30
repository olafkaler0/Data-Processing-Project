# main.py

from fetcher import fetch_data
from processor import process_data
from saver import save_data

def main():
    api_url = "https://api.example.com/data"
    username = "miranda-irving@hotmail.com"
    password = "Bande2131"
    output_file = "processed_data.json"
    
    data = fetch_data(api_url, username, password)
    processed_data = process_data(data)
    if processed_data:
        save_data(output_file, processed_data)
        print("Data processing and saving completed successfully.")
    else:
        print("Data processing failed.")

if __name__ == "__main__":
    main()
