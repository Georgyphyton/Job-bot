from aiogram import Bot, types


async def get_start(message: types.Message, bot: Bot) -> None:
    user_link = f"https://t.me/{message.from_user.username}"
    await bot.send_message(
        message.chat.id,
        f'''Hi <b><a href="{user_link}">{message.from_user.full_name}</a></b>!''',
        parse_mode='html',
        disable_web_page_preview=1)
