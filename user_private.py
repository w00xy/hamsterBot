from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command

from bot.config import SITE_URL
from kbds.inline import get_url_btns

user_private_router = Router()


@user_private_router.message(CommandStart())
@user_private_router.message(Command('app'))
async def start_message(message: types.Message):
    await message.answer('Get FREE keys for Hamster Combat ride game.\n\n'
                         '<b>Run the app</b> 👇',
                         reply_markup=get_url_btns(
                             btns={'Take keys🔑': SITE_URL}
                         ))


@user_private_router.message(F.photo)
async def get_photo(message: types.Message):
    if message.photo:
        await message.answer(f'ID фото: {message.photo[-1].file_id}')
