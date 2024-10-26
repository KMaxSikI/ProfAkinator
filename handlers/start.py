from aiogram import types, Dispatcher
from career_bot.keyboards import start_keyboard


async def start_command(message: types.Message):
    await message.answer(
        "Привет! Я профориентационный бот-акинатор. Проходя тест, вы сможете узнать, какая профессия вам подходит. Нажмите 'Начать тест', чтобы узнать больше!",
        reply_markup=start_keyboard()
    )


def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(start_command, commands="start")
