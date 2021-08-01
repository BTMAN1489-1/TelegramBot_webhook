from aiogram import types
from data import bot_commands


async def set_default_commands(dp):
    await dp.bot.set_my_commands(commands=bot_commands.default_command, scope=types.BotCommandScopeDefault())
