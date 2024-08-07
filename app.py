import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties

from bot_cmds_list import private
from config import TOKEN
from user_private import user_private_router

# разрешенные методы общения с ботом
allowed_updates = ['message, callback_query']


async def on_shutdown():
    print('Бот лёг')


async def main():
    # bot setting
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
    bot.my_admins_list = []

    dp = Dispatcher()

    # on_start_up and shotdown functions dasdsa
    dp.shutdown.register(on_shutdown)

    # drop offline messages
    await bot.delete_webhook(drop_pending_updates=True)

    dp.include_router(user_private_router)

    # кнопки из меню справа снизу
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())

    await dp.start_polling(bot, allowed_updates=allowed_updates)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
