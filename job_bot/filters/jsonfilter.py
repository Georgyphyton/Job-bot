from aiogram.filters import Filter
from aiogram import types
import json


class FilterNotJson(Filter):
    async def __call__(self, message: types.Message) -> bool:
        try:
            json.loads(message.text)
            return False
        except Exception:
            return True
