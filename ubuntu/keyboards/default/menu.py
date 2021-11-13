from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="600r")
        ],
        [
            KeyboardButton(text="400r"),
            KeyboardButton(text="200r")
        ]
    ],
    resize_keyboard=True
)