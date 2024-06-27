from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()
api_key = os.getenv('API_KEY')

def fetch_data(api_url, params):
    response = requests.get(api_url, params=params)
    if response.status_code == 200: #if status is ok
        return response.json()
    else:
        response.raise_for_status()

def save_data(data, filepath):
    with open(filepath, 'w') as f:
        json.dump(data, f)

if __name__ == "__main__":
    api_url = 'https://api.openchargemap.io/v3/poi'
    params = {
            'key': api_key,
            'output': 'json',
            'countrycode': ['PL', 'DE'],
            'maxresults': 26000 #for PL 1000 is sufficient, 25000 for DE is ok
            }
    data = fetch_data(api_url, params)
    save_data(data, "../data/raw/raw_data.json") #.. means "go up one directory"