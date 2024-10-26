import sqlite3

# Путь к базе данных
db_path = 'akinator_bot.db'

# Подключение к базе данных
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Словарь соответствия для каждого question_id и short_answer
answer_mappings = {
    1: ['A', 'B', 'C', 'D'],  # Ответы для question_id = 1
    2: ['A', 'B', 'C', 'D'],  # Ответы для question_id = 2
    3: ['A', 'B', 'C', 'D'],
    4: ['A', 'B', 'C', 'D'],
    5: ['A', 'B', 'C', 'D'],
    6: ['A', 'B', 'C', 'D'],
    7: ['A', 'B', 'C', 'D'],
    8: ['A', 'B', 'C', 'D'],
    9: ['A', 'B', 'C', 'D'],
    10: ['A', 'B', 'C', 'D'],
    11: ['A', 'B', 'C', 'D'],
    12: ['A', 'B', 'C', 'D'],
    13: ['A', 'B', 'C', 'D'],
    14: ['A', 'B', 'C', 'D'],
    15: ['A', 'B', 'C', 'D'],
    16: ['A', 'B', 'C', 'D'],
    17: ['A', 'B', 'C', 'D'],
    18: ['A', 'B', 'C', 'D'],
    19: ['A', 'B', 'C', 'D'],
    20: ['A', 'B', 'C', 'D'],
    21: ['A', 'B', 'C', 'D'],
    22: ['A', 'B', 'C', 'D'],
    23: ['A', 'B', 'C', 'D'],
    24: ['A', 'B', 'C', 'D'],
    25: ['A', 'B', 'C', 'D'],
    26: ['A', 'B', 'C', 'D'],
    27: ['A', 'B', 'C', 'D'],
    28: ['A', 'B', 'C', 'D'],
    29: ['A', 'B', 'C', 'D'],
    30: ['A', 'B', 'C', 'D'],
    31: ['A', 'B', 'C', 'D'],
    32: ['A', 'B', 'C', 'D'],
    33: ['A', 'B', 'C', 'D'],
    34: ['A', 'B', 'C', 'D'],
    35: ['A', 'B', 'C', 'D'],
    36: ['A', 'B', 'C', 'D'],
    37: ['A', 'B', 'C', 'D'],
    38: ['A', 'B', 'C', 'D'],
    39: ['A', 'B', 'C', 'D'],
    40: ['A', 'B', 'C', 'D'],
    41: ['A', 'B', 'C', 'D'],
    42: ['A', 'B', 'C', 'D'],
    43: ['A', 'B', 'C', 'D'],
    44: ['A', 'B', 'C', 'D'],
    45: ['A', 'B', 'C', 'D'],
    46: ['A', 'B', 'C', 'D'],
    47: ['A', 'B', 'C', 'D'],
    48: ['A', 'B', 'C', 'D'],
    49: ['A', 'B', 'C', 'D'],
    50: ['A', 'B', 'C', 'D'],
    51: ['A', 'B', 'C', 'D'],
    52: ['A', 'B', 'C', 'D'],
    53: ['A', 'B', 'C', 'D'],
    54: ['A', 'B', 'C', 'D'],
    55: ['A', 'B', 'C', 'D'],
    56: ['A', 'B', 'C', 'D'],
    57: ['A', 'B', 'C', 'D'],
    58: ['A', 'B', 'C', 'D'],
    59: ['A', 'B', 'C', 'D'],
    60: ['A', 'B', 'C', 'D'],
    61: ['A', 'B', 'C', 'D'],
    # Добавьте аналогично для других вопросов
}

# Обновление столбца short_answer
for question_id, short_answers in answer_mappings.items():
    for idx, short_answer in enumerate(short_answers):
        cursor.execute("""
            UPDATE answers
            SET short_answer = ?
            WHERE question_id = ? AND ROWID = (
                SELECT ROWID FROM answers WHERE question_id = ? LIMIT 1 OFFSET ?
            )
        """, (short_answer, question_id, question_id, idx))

# Сохранение и закрытие
conn.commit()
conn.close()
print("Поле 'short_answer' успешно заполнено.")