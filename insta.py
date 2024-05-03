import os
import requests
from dotenv import load_dotenv

load_dotenv()


def instadownload(link):
    url = "https://instagram-downloader-download-photo-video-reels-igtv.p.rapidapi.com/data"

    querystring = {"url": link}

    headers = {
        "X-RapidAPI-Key": os.getenv("RapidApi-Key"),
        "X-RapidAPI-Host": "instagram-downloader-download-photo-video-reels-igtv.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    rest = response.json()['data']['result']['video_url']
    if response.status_code == 200:
        dict = {'video': rest}
        return dict
    else:
        return 'No'
