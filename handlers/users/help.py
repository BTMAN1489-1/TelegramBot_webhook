from aiogram import types, md
from aiogram.dispatcher.filters.builtin import CommandHelp
from aiogram.utils import emoji
import asyncio
from loader import dp
from data import dialogs
import asyncio
from utils.misc import delete_messages


@dp.message_handler(CommandHelp(), state="*")
async def bot_help(message: types.Message):
    reply = await message.reply(
        emoji.emojize(dialogs.bot_response['help_text'].format(
            botname=md.hbold((await message.bot.me).full_name))))

    asyncio.create_task(delete_messages(message)) and asyncio.create_task(
        delete_messages(reply)) if message.chat.type != "private" else False
