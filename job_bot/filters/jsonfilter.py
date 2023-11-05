from aiogram.filters import Filter
from datetime import datetime
from job_bot.data.active_db import max_time, min_time
from aiogram import types
import json


class FilterNotJson(Filter):
    async def __call__(self, message: types.Message) -> bool:
        try:
            json.loads(message.text)
            return False
        except Exception:
            return True


class FilterDict(Filter):
    group_type = ['month', 'day', 'hour']

    async def __call__(self, message: types.Message) -> bool:
        mes_dict = json.loads(message.text)
        try:
            dt_from = datetime.strptime(mes_dict.get('dt_from'), "%Y-%m-%dT%H:%M:%S")
            dt_upto = datetime.strptime(mes_dict.get('dt_upto'), "%Y-%m-%dT%H:%M:%S")
        except Exception:
            return True
        rule1 = len(mes_dict) == 3
        rule2 = mes_dict.get('group_type') in self.group_type
        rule3 = dt_from >= min_time
        rule4 = dt_upto <= max_time
        return not rule1 or not rule2 or not rule3 or not rule4
