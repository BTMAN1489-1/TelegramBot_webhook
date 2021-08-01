from aiogram import types, md
from aiogram.dispatcher.filters import Command, AdminFilter
from loader import dp
from data import dialogs
import asyncio
from utils.misc import delete_messages


@dp.message_handler(AdminFilter(), Command("commands"), state="*")
async def send_commands(message: types.Message):
    bot = message.bot
    commands = await bot.get_my_commands(scope=types.BotCommandScopeAllChatAdministrators())

    await bot.send_message(chat_id=message.from_user.id, text="".join((dialogs.bot_response['commands_text'], '\n'.join(
        map(lambda command: f"<b>/{md.quote_html(command.command)}</b>: <b>{command.description}</b>", commands)))),
                           reply_to_message_id=message.message_id, allow_sending_without_reply=True)

    asyncio.create_task(delete_messages(message, 0))


@dp.message_handler(Command("commands"), state="*")
async def send_commands(message: types.Message):
    bot = message.bot
    commands = await bot.get_my_commands(scope=types.BotCommandScopeDefault())
    await bot.send_message(chat_id=message.from_user.id, text="".join((dialogs.bot_response['commands_text'], '\n'.join(
        map(lambda command: f"<b>/{md.quote_html(command.command)}</b>: <b>{command.description}</b>", commands)))),
                           reply_to_message_id=message.message_id, allow_sending_without_reply=True)

    asyncio.create_task(delete_messages(message, 0)) if message.chat.type != "private" else False
