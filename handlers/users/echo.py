from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp


# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
@dp.message_handler(state="*")
async def bot_echo_all(message: types.Message, state: FSMContext):
    await message.answer(message.text)
