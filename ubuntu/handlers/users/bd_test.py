import random

from aiogram import types
from aiogram.dispatcher.filters import Command
from asyncpg import Connection, Record
from asyncpg.exceptions import UniqueViolationError
from ubuntu.loader import bot, dp, db

class DBCommands:
    pool: Connection = db
    ADD_NEW_USER = "INSERT INTO users(chat_id, username, full_name) VALUES ($1, $2, $3) RETURNING id"
    ADD_NEW_USER_REFERRAL = "INSERT INTO users(chat, username, full_name, referral)" \
                            "values ($1, $2, $3, $4) RETURNING id"
    COUNT_USERS = "SELECT COUNT(*) FROM users"
    GET_ID = "select id from users where chat_id = $1"
    CHECK_REFERRALS = "select chat_id from users where referral="\
                      "(select id from users where chat_id=$1)"
    CHECK_BALANCE = "Select balance from users where chat_id = $1"
    ADD_MONEY = "update users set balance=balance+$1 where chat_id =$2"

    async def add_new_user(self, referral=None):
        user = types.User.get_current()
        chat_id = user.id
        username = user.username
        full_name = user.full_name
        args = chat_id, username, full_name
        if referral:
            args += (int(referral),)
            command = self.ADD_NEW_USER
        else:
            command = self.ADD_NEW_USER

        try:
            record_id = await self.pool.fetchval(command, *args)
            return record_id
        except UniqueViolationError:
            pass

    async def count_users(self):
        record: Record = await self.pool.fetchval(self.COUNT_USERS)
        return record

    async def get_id(self):
        command = self.GET_ID
        user_id = types.User.get_current().id
        return await self.pool.fetchval(command, user_id)

    async def check_referrals(self):
        user_id = types.User.get_current().id
        command = self.CHECK_REFERRALS
        rows = await self.pool.fetch(command, user_id)
        text = ""
        for num, row in enumerate(rows):
            chat = await bot.get_chat(row["chat_id"])
            user_link = chat.get_mention(as_html=True)
            text += str(num + 1) + ". " + user_link
        return text

    async def check_balance(self):
        command = self.CHECK_BALANCE
        user_id = types.User.get_current().id
        return await self.pool.fetchval(command, user_id)

    async def add_money(self, money):
        command = self.ADD_MONEY
        user_id = types.User.get_current().id
        return await self.pool.fetchval(command, money, user_id)

database = DBCommands()


@dp.message_handler(commands=["start"])
async def register_user(message: types.Message):
    chat_id = message.from_user.id
    referral = message.get_args()
    id = await database.add_new_user(referral=referral)
    count_users = await database.count_users()

    text = ""
    if not id:
        id = await database.get_id()
    else:
        text = "Записан в базу"
    bot_username = (await bot.get_me()).username
    id_referral = id
    bot_link = f"https://t.me/{bot_username}?state={id_referral}"
    balance = await database.check_balance()
    text += f"""
Сейчас в базе {count_users} человек!

Ваша реферальная ссылка: {bot_link}
Проверить реферралов можно по команде: /referrals

Ваш баланс: {balance} монет.
Добавить монет: /add_money    
"""
    await bot.send_message(chat_id=chat_id, text=text)

@dp.message_handler(Command("referrals"))
async def check_referrals(message: types.Message):
    referrals = await database.check_referrals()
    text = ''
    if referrals == '':
        text += "У Вас нет рефералов"
    else:
        text += "Ваши рефералы: \n" + referrals
    await message.answer(text)

@dp.message_handler(Command("add_money"))
async def add_money(message: types.Message):
    random_amount = random.randint(1, 100)
    await database.add_money(random_amount)
    balance = await database.check_balance()
    text = "Вам было добавлено {money} монет.\nТеперь ваш баланс: {balance}".format(money=random_amount,balance=balance)
    await message.answer(text)
