import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.choice_buttons import choice, pear_keyboard, apples_keyboard
from ubuntu.loader import dp

@dp.message_handler(Command("items"))
async def show_items(message: Message):
    await message.answer(text="Выберите товар:", reply_markup=choice)

@dp.callback_query_handler(buy_callback.filter(item_name="apple"))
async def buying_apples(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"call = {callback_data}")
    quantity = callback_data.get("quantity")
    await call.message.answer(f"You chose apple, count of apples: {quantity}. Thank you!",
                              reply_markup=apples_keyboard)

@dp.callback_query_handler(text_contains="pear")
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=6)
    callback_data = call.data
    await call.message.answer(f"You chose PEAR {callback_data}", reply_markup=pear_keyboard)

@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    await call.answer("You cancel purchase!", show_alert=True)
    await call.message.edit_reply_markup()