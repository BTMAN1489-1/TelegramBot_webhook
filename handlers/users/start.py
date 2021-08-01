from aiogram import types, md
from aiogram.utils import emoji
from aiogram.dispatcher.filters import CommandStart, ChatTypeFilter
from data import dialogs
from loader import dp


@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), CommandStart(), state="*")
async def bot_start(message: types.Message):
    await message.answer(emoji.emojize(
        dialogs.bot_response['start_text'].format(username=md.hbold(message.from_user.full_name))))
