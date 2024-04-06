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
        if data['type'] == 'image':
            await message.answer_photo(photo=data['media'])
        elif data['type'] == 'video':
            await message.answer_video(video=data['media'])
        elif data['type'] == 'carousel':
            for i in data['media']:
                await message.answer_document(document=i)
        elif data['type'] == 'story-video':
            await message.answer_video(video=data['media'])
        elif data['type'] == 'story-image':
            await message.answer_photo(photo=data['media'])
        else:
            await message.answer('Bu havola orqali hech narsa topilmadi')


