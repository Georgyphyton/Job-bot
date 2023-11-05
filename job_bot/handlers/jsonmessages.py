from aiogram import Bot, types


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
