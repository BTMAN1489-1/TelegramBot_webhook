from aiogram import types

default_command = [types.BotCommand("help", "Введите для получения справочной информации"),
                   types.BotCommand("commands", "Введите для получения списка доступных команд в вашем приватном чате с ботом"),
                   types.BotCommand("cancel", 'Введите для отмены действия')]

