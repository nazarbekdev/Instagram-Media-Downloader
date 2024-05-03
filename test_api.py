import requests
from pprint import pprint as pp
url = "https://instagram-downloader-download-photo-video-reels-igtv.p.rapidapi.com/data"

querystring = {"url": "https://www.instagram.com/reel/C5qsmmYsEYc/?igsh=MWtxN3hpazdsMmZ0cA=="}

headers = {
    "X-RapidAPI-Key": "af0a9a4d97mshf5d4fc239774059p147199jsnf1c8c0a3a5ea",
    "X-RapidAPI-Host": "instagram-downloader-download-photo-video-reels-igtv.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

pp(response.json()['data']['result']['video_url'])
