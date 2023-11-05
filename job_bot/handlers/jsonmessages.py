from aiogram import Bot, types
from datetime import datetime
from dateutil.relativedelta import relativedelta
from job_bot.data.active_db import coll
import json


async def get_start(message: types.Message, bot: Bot) -> None:
    user_link = f"https://t.me/{message.from_user.username}"
    await bot.send_message(
        message.chat.id,
        f'''Hi <b><a href="{user_link}">{message.from_user.full_name}</a></b>!''',
        parse_mode='html',
        disable_web_page_preview=1)


async def answer_not_json(message: types.Message) -> None:
    await message.answer('''Невалидный запос. Пример запроса:
{"dt_from": "2022-09-01T00:00:00", "dt_upto":
"2022-12-31T23:59:00","group_type": "month"}''')


async def answer_invalid_format(message: types.Message) -> None:
    await message.answer('''Допустимо отправлять только следующие запросы:
{"dt_from": "2022-09-01T00:00:00", "dt_upto":
"2022-12-31T23:59:00", "group_type": "month"}
{"dt_from": "2022-10-01T00:00:00", "dt_upto":
"2022-11-30T23:59:00", "group_type": "day"}
{"dt_from": "2022-02-01T00:00:00", "dt_upto":
"2022-02-02T00:00:00", "group_type": "hour"}''')


async def get_result(message: types.Message) -> None:
    mes_dict = json.loads(message.text)
    dt = mes_dict['group_type']
    min_time = datetime.strptime(mes_dict['dt_from'], "%Y-%m-%dT%H:%M:%S")
    max_time = datetime.strptime(mes_dict['dt_upto'], "%Y-%m-%dT%H:%M:%S")
    formats = {'month': ["%Y-%m-01T00:00:00", relativedelta(months=1)],
               'day': ["%Y-%m-%dT00:00:00", relativedelta(days=1)],
               'hour': ["%Y-%m-%dT%H:00:00", relativedelta(hours=1)]}

    agr_data = list(coll.aggregate([
        {"$match": {"dt": {"$gte": min_time, "$lte": max_time}}},
        {"$group":
         {
             "_id": {"$dateToString": {
                 "format": formats[dt][0], 'date': '$dt'}},
             "Total_Price": {"$sum": "$value"}
         }},
        {"$sort": {'_id': 1}},
        {"$group":
         {
             '_id': 1,
             "dataset": {"$push": '$Total_Price'},
             "labels": {"$push": "$_id"}
         }},
        {"$project":
         {"_id": 0, "dataset": 1, "labels": 1}}
    ]))[0]
    await message.answer(json.dumps(agr_data))
