import pandas as pd
from db import Session, Profession, Question, Answer

# Ссылки на Google Sheets, опубликованные в формате CSV
professions_sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ0vWKQ1Wfya4nVFkjri5j-On2ahV3JOu8nIThpIALEfvkQiJqxzxDurvwVPAnwqXm0kI1IjqjtFyWX/pub?gid=1587945699&single=true&output=csv"
test_sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vStgWKCBgjN5mR-jqH6_WSkLog9PfD3HluO_TXTsVM7CCvNptP4M76-pq1u4_FAp9BPxLnJPetWvHt5/pub?gid=840570321&single=true&output=csv"

# Функция для загрузки данных о профессиях
def load_professions_from_google_sheet():
    data = pd.read_csv(professions_sheet_url)
    session = Session()
    session.query(Profession).delete()  # Очищаем старые данные профессий

    for _, row in data.iterrows():
        profession = Profession(
            name=row['Профессии'],
            specialty=row['Специальность'],
            category=row['Категория'],
            description=row['Описание'],
            skills=row['Умения'],
            technologies=row['Технологии'],
            recommendations=row['Рекомендации']
        )
        session.add(profession)

    session.commit()
    session.close()
    print("Данные о профессиях успешно загружены из Google Sheets")

# Функция для загрузки вопросов и ответов из Google Sheets
def load_questions_and_answers_from_google_sheet():
    data = pd.read_csv(test_sheet_url)
    session = Session()
    session.query(Question).delete()  # Очищаем старые данные вопросов
    session.query(Answer).delete()    # Очищаем старые данные ответов

    question_id = None
    for _, row in data.iterrows():
        if pd.notna(row['Вопросы']):
            question = Question(text=row['Вопросы'])
            session.add(question)
            session.flush()
            question_id = question.id

        if pd.notna(row['Ответы']) and pd.notna(row['Профессии и баллы']):
            answer = Answer(
                question_id=question_id,
                text=row['Ответы'],
                professions_scores=row['Профессии и баллы']
            )
            session.add(answer)

    session.commit()
    session.close()
    print("Вопросы и ответы успешно загружены из Google Sheets")

if __name__ == "__main__":
    load_professions_from_google_sheet()
    load_questions_and_answers_from_google_sheet()