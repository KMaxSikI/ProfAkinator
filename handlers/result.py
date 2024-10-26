from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from services.result_service import calculate_result
from career_bot.loader import dp


async def show_result(message: types.Message, state: FSMContext):
    result_text = calculate_result(user_id=message.from_user.id)
    await message.answer(result_text, reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add("Повторить тест", "Завершить тест"))
    await state.finish()


async def end_test(message: types.Message, state: FSMContext):
    # Очистка состояния и удаление клавиатуры
    await state.finish()
    await message.answer(
        "Спасибо, что приняли участие в тестировании! Успехов вам в изучении выбранной профессии. "
        "Если хотите пройти тест ещё раз, нажмите на /start.",
        reply_markup=types.ReplyKeyboardRemove()
    )


# Функция для регистрации хендлеров в `result.py`
def register_handlers_result(dp: Dispatcher):
    dp.register_message_handler(show_result, text="Показать результат")
    dp.register_message_handler(end_test, text="Завершить тест")