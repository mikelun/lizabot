from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.Test import Test


@dp.message_handler(Command("test"), state=None)
async def enter_test(message: types.Message):
    await message.answer("Вопрос 1. \n"
                         "Тяночка или мужик?")
    await Test.Q1.set()

@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["ans1"] = answer
    await message.answer("Вопрос 2. \n"
                         "Ваш возраст: ")
    await Test.next()

@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    answer2 = message.text
    data = await state.get_data()
    answer1 = data.get("ans1")
    await message.answer("Thank you for answers!"
                         f"Your answers: {answer1} and {answer2}")
    await state.finish()