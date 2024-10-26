from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def start_keyboard():
    return ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("Начать тест"))

def answer_keyboard():
    return ReplyKeyboardMarkup(resize_keyboard=True).row(
        KeyboardButton("A"), KeyboardButton("B"), KeyboardButton("C"), KeyboardButton("D")
    )

def end_test_keyboard():
    return ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton("Повторить тест"), KeyboardButton("Завершить тест")
    )
