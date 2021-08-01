from aiogram.types import ContentType, Message
from loader import dp
import asyncio
from utils.misc import delete_messages


@dp.message_handler(
    content_types=(ContentType.DELETE_CHAT_PHOTO, ContentType.NEW_CHAT_PHOTO, ContentType.NEW_CHAT_TITLE,
                   ContentType.LEFT_CHAT_MEMBER))
async def bot_start(message: Message):
    asyncio.create_task(delete_messages(message, 60))
