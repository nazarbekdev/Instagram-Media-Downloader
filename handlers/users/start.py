from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    with open('user.txt', 'a') as fl:
        fl.writelines(message.from_user.full_name)
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!\nBotga havola yuboring.")
