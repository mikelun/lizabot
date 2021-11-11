from loader import dp
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu
from aiogram.dispatcher.filters import Command, Text

@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Выберите время подписки", reply_markup=menu)

@dp.message_handler(Text(equals=["600r", "200r", "400r"]))
async def get_subscribe(message: Message):
    await message.answer(f"You chose {message.text}. Thank you!", reply_markup=ReplyKeyboardRemove())