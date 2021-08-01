from aiogram import types, md
from loader import dp
from data import dialogs
import asyncio
from utils.misc import delete_messages


@dp.message_handler(state="*", content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
async def new_member_handler(message: types.Message):
    for member in message.new_chat_members:
        if not member.is_bot:
            reply = await message.answer(
                text=dialogs.bot_response['welcome'].format(username=md.hbold(member.full_name),
                                                            chatname=md.hbold(message.chat.full_name)))
            asyncio.create_task(delete_messages(message, 60)) and asyncio.create_task(delete_messages(reply, 60))

