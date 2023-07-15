import json
import requests


def instadownload(link):

    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"


    querystring = {"url": link}

    headers = {
	"X-RapidAPI-Key": "3cf5245db4msh0ac39c5060f55c5p1afbf6jsnb48b55475d0f",
	"X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
}

    response = requests.get(url, headers=headers, params=querystring)
    rest = json.loads(response.text)
    dict = {}

    if 'Type' in rest.keys():
        if rest['Type'] == 'Post-Video':
            dict['type'] = 'video'
            dict['media'] = rest['media']
            return dict
        elif rest['Type'] == 'Post-Image':
            dict['type'] = 'image'
            dict['media'] = rest['media']
            return dict
        elif rest['Type'] == 'Carousel':
            dict['type'] = 'carousel'
            dict['media'] = rest['media']
            return dict
        elif rest['stories'][0]['Type'] == 'Story-Video':
            dict['type'] = 'story-video'
            dict['media'] = rest['stories'][0]['media']
            return dict
        else:
            return 'No'
    elif 'stories' in rest.keys():
        if rest['stories'][0]['Type'] == 'Story-Video':
            dict['type'] = 'story-video'
            dict['media'] = rest['stories'][0]['media']
            # for i in range(len(rest['stories'])):
            #     dict['media'] = rest['stories'][i]['media']
            return dict
        elif rest['stories'][0]['Type'] == 'Story-Image':
            dict['type'] = 'story-image'
            dict['media'] = rest['stories'][0]['media']
            # for i in range(len(rest['stories'])):
            #     dict['media'] = rest['stories'][i]['media']
            return dict
    else:
        return 'No'
#     return rest['stories']
#
#
# pp(instadownload('https://www.instagram.com/stories/sherali_12_13/3144999608330379198/'))
