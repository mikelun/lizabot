from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import callback_data

from keyboards.inline.callback_datas import buy_callback

# choice = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text="Buy tyan", callback_data=buy_callback.new(item_name="pear", quantity=1))
#         ],
#         [
#             InlineKeyboardButton(text="Buy bread", callback_data="")
#         ],
#         [
#             InlineKeyboardButton(text="Buy anime", callback_data="")
#         ],
#     ]
# )

choice = InlineKeyboardMarkup(row_width=1)
buy_pear = InlineKeyboardButton(text="Купить грушу", callback_data="buy:pear:5")
buy_apple = InlineKeyboardButton(text="Купить яблоко", callback_data="buy:apple:5")
cancel = InlineKeyboardButton(text="Отмена", callback_data="cancel")

choice.insert(buy_pear)
choice.insert(buy_apple)
choice.insert(cancel)

pear_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Buy now", url="https://google.com")
        ]
    ]
)

apples_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Buy now", url="https://yandex.ru")
        ]
    ]
)