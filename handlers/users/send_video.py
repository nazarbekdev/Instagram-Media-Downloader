import time

from loader import bot, dp

from aiogram import types
from aiogram.dispatcher.filters import Text
from insta import instadownload
from youtube import yuotubelink
from yt import youtube_data


@dp.message_handler(Text(startswith='https://www.instagram.com/'))
async def send_media(message: types.Message):
    await message.answer('Iltimos kuting!')
    time.sleep(3)
    await message.answer('🔍 Media topilmoqda...')
    link = message.text
    data = instadownload(link=link)
    if data == 'No':
        await message.answer("Bu havola orqali hech narsa topilmadi 😔")
    else:
        await message.answer_video(video=data['video'],
                                   caption='📥 Video @instagram_video_downloaderbot orqali yuklab olindi.')


@dp.message_handler(Text(startswith=['https://youtube.com/', 'https://www.youtube.com/', 'https://youtu.be/']))
async def youtube_video(message: types.Message):
    await message.answer('Iltimos kuting!')
    link = message.text
    data = youtube_data(url_link=link)
    time.sleep(2)
    await message.answer('🔍 Media topilmoqda...')
    if data == 'No':
        await message.answer('Bu havola orqali hech narsa topilmadi 😔')
    else:
        await message.answer_video(video=data['video'], caption=data['title'])
        await message.answer_audio(audio=data['audio'],
                                   caption='📥 Audio @instagram_video_downloaderbot orqali yuklab olindi.')
