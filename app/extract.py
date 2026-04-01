import pandas as pd
import requests
import os

def fetch_users():
    limit = 30
    skip = 0
    users_list = []

    print("############# Fetching Is Started ##########")

    while True:
        url = f'https://dummyjson.com/users?limit={limit}&skip={skip}'
        response = requests.get(url)
        users = response.json()['users']

        if not users:
            break

        users_list.extend(users)
        skip += limit

    # Convert to DataFrame
    df = pd.json_normalize(users_list)
    print("############# Fetching DONE ! ##########")

    # --- Save raw data ---
    os.makedirs("output/data", exist_ok=True)
    df.to_csv("output/data/users_raw.csv", index=False)
    print("############# Raw data is saved in output/data/users_raw.csv ##########")

    return users_list