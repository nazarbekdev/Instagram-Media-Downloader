import requests
import os


def yuotubelink(url_link):
    url = "https://auto-download-all-in-one.p.rapidapi.com/v1/social/autolink"

    payload = {"url": url_link}
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": os.getenv('YouTube-Key'),
        "X-RapidAPI-Host": "auto-download-all-in-one.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        video_url = response.json()['medias'][0]['url']
        author = response.json()['author']
        video_duration = int(response.json()['duration'])
        video_extension = response.json()['medias'][0]['extension']
        video_quality = response.json()['medias'][0]['quality']
        video_title = response.json()['title']
        audio_extension = response.json()['medias'][-1]['extension']
        audio_url = response.json()['medias'][-1]['url']

        hour = video_duration // 3600
        minute = (video_duration % 3600) // 60
        second = video_duration % 60

        if video_duration >= 3600:
            duration = f'{hour}:{minute}:{second}'
        else:
            duration = f'{minute}:{second}'

        url_info = f"""
Kanal nomi: {author}
Video mavzusi: {video_title}
Video davomiyligi: {duration}
Video turi: {video_extension}
Video sifati: {video_quality}
        """
        url_data = {
            'video_url': video_url,
            'audio_url': audio_url,
            'video_data': url_info,
            'audio_extension': audio_extension,
        }
        print(url_data)
        return url_data
    else:
        return 'No'
