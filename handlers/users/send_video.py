import time

from loader import bot, dp

from aiogram import types
from aiogram.dispatcher.filters import Text
from insta import instadownload


@dp.message_handler(Text(startswith='https://www.instagram.com/'))
async def send_media(message: types.Message):
    await message.answer('Iltimos kuting!')
    time.sleep(3)
    await message.answer('Media topilmoqda...')
    link = message.text
    data = instadownload(link=link)
    if data == 'No':
        await message.answer("Bu havola orqali hech narsa topilmadi")
    else:
        await message.answer_video(video=data['video'])
