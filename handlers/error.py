from aiogram import types, Dispatcher

# Функция для обработки сообщений, которые не соответствуют ожиданиям бота
async def handle_unexpected_message(message: types.Message):
    await message.answer("Я понимаю только команды и ответы в рамках теста. Пожалуйста, используйте кнопки для ответов.")

def register_handlers_errors(dp: Dispatcher):
    dp.register_message_handler(handle_unexpected_message, content_types=types.ContentType.ANY)