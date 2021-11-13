import asyncio
import asyncpg
import logging

from data.config import HOST, PG_PASS, PG_USER

async def create_db():
    create_db_command = open("create_db.sql", "r").read()
    logging.info("Connecting to db.")
    conn: asyncpg.Connection = await asyncpg.connect(
        user=PG_USER,
        password=PG_PASS,
        host=HOST
    )
    await conn.execute(create_db_command)
    logging.info("Table has been created!")
    await conn.close()

async def make_pool():
    return await asyncpg.create_pool(
        user=PG_USER,
        password=PG_PASS,
        host=HOST
    )


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_db())