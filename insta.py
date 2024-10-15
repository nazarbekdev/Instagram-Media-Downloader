import os
import requests
from dotenv import load_dotenv
load_dotenv()


def instadownload(link):
    url = "https://instagram-downloader36.p.rapidapi.com/instagram"

    querystring = {"insta_url": link}

    headers = {
        "x-rapidapi-key": os.getenv("RapidApi-Key"),
        "x-rapidapi-host": "instagram-downloader36.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    rest = response.json()['urls'][0]['download_url']
    if response.status_code == 200:
        dict = {'video': rest}
        return dict
    else:
        return 'No'
