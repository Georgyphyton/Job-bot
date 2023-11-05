from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from job_bot.handlers import jsonmessages
from job_bot.filters.jsonfilter import FilterNotJson, FilterDict
from dotenv import load_dotenv
import os
import logging
import asyncio

load_dotenv()
TOKEN = os.getenv('TOKEN',)


async def start() -> None:
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.message.register(jsonmessages.get_start, CommandStart())
    dp.message.register(jsonmessages.answer_not_json, FilterNotJson())
    dp.message.register(jsonmessages.answer_invalid_format, FilterDict())
    dp.message.register(jsonmessages.get_result)
    logging.basicConfig(level=logging.INFO)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
