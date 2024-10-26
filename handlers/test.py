from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from career_bot.db import Session, UserTestRecord
from services.test_service import get_question, process_answer
from services.result_service import calculate_result
from career_bot.keyboards import answer_keyboard, end_test_keyboard

# Словарь для отслеживания текущего вопроса и сессии пользователя
user_question_index = {}
user_session = {}

async def start_test(message: types.Message, state: FSMContext):
    await state.finish()  # Очищаем состояние, если пользователь повторяет тест
    user_id = message.from_user.id
    user_question_index[user_id] = 1  # Устанавливаем начальный вопрос для пользователя

    # Создаем новую сессию для прохождения теста
    session = Session()
    new_session_id = (
        session.query(UserTestRecord)
        .filter_by(user_id=user_id)
        .count() + 1  # Увеличиваем session_id для каждого нового прохождения
    )
    user_session[user_id] = new_session_id
    session.close()

    question_text, answers = get_question(user_question_index[user_id])

    if question_text and answers:
        answer_texts = "\n".join([f"{answer.text}" for answer in answers])
        await message.answer(f"{question_text}\n\n{answer_texts}", reply_markup=answer_keyboard())
    else:
        await message.answer("Вопросов не найдено. Попробуйте позже.")

async def answer_handler(message: types.Message):
    user_id = message.from_user.id
    current_question_id = user_question_index.get(user_id, 1)
    answer_text = message.text

    result = process_answer(user_id, current_question_id, answer_text, session_id=user_session[user_id])

    if result["next_question"]:
        user_question_index[user_id] += 1
        next_question_id = user_question_index[user_id]

        question_text, answers = get_question(next_question_id)

        if question_text and answers:
            answer_texts = "\n".join([f"{answer.text}" for answer in answers])
            await message.answer(f"{question_text}\n\n{answer_texts}", reply_markup=answer_keyboard())
        else:
            await show_final_result(message)
    else:
        await show_final_result(message)

async def show_final_result(message: types.Message):
    user_id = message.from_user.id
    result_text = calculate_result(user_id, user_session[user_id])
    await message.answer(result_text, reply_markup=end_test_keyboard())
    del user_question_index[user_id]
    del user_session[user_id]

# Обработчик для кнопки "Повторить тест"
async def repeat_test(message: types.Message, state: FSMContext):
    await start_test(message, state)  # Повторный запуск теста с начального состояния

def register_handlers_test(dp: Dispatcher):
    dp.register_message_handler(start_test, text="Начать тест")
    dp.register_message_handler(answer_handler, lambda message: message.text in ["A", "B", "C", "D"])
    dp.register_message_handler(repeat_test, text="Повторить тест")