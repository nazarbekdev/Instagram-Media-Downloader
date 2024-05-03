import requests
import os


def youtube_data(url_link):
    urd_id = url_link.split('?')[0].split('/')[-1]
    url = "https://youtube-media-downloader.p.rapidapi.com/v2/video/details"

    querystring = {"videoId": urd_id}

    headers = {
        "X-RapidAPI-Key": os.getenv('You_tube_key'),
        "X-RapidAPI-Host": "youtube-media-downloader.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        video = response.json()['videos']['items'][1]['url']
        audio = response.json()['audios']['items'][1]['url']
        title = response.json()['title']
        url_data = {
            "video": video,
            "audio": audio,
            "title": title
        }
        return url_data
    else:
        return 'No'
