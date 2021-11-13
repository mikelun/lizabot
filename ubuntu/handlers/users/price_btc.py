import asyncio

from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from requests import get
from bs4 import BeautifulSoup

from ubuntu.loader import dp

@dp.message_handler(Command("btc"))
async def crypto_btc(message: Message):
    url = "https://www.investing.com/crypto/bitcoin/btc-usd"
    headers = headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    async def btc_price():
        while True:
            await asyncio.sleep(5)
            response = get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            price = soup.find(id='last_last').text
            await message.answer(price)

    task1 = asyncio.create_task(btc_price())
    await task1

