from career_bot.db import Session, Question, Answer, UserTestRecord
from sqlalchemy.orm import joinedload


# Функция для получения вопроса и вариантов ответов
def get_question(question_id):
    session = Session()
    question = session.query(Question).options(joinedload(Question.answers)).filter(Question.id == question_id).first()

    if question:
        answers = question.answers  # Ответы для вопроса уже загружены
        question_text = question.text
    else:
        question_text, answers = None, None

    session.close()
    return question_text, answers


# Функция для обработки ответа пользователя и сохранения данных
def process_answer(user_id, question_id, answer_text, session_id):
    session = Session()

    answer = session.query(Answer).filter(
        Answer.question_id == question_id,
        Answer.short_answer == answer_text
    ).first()

    if not answer:
        session.close()
        return {"next_question": True}

    # Обновляем или создаем запись для текущей сессии
    for prof_score in answer.professions_scores.split("\n"):
        try:
            prof, score = prof_score.split(" = ")
            score = float(score)
        except ValueError:
            continue

        record = session.query(UserTestRecord).filter_by(
            user_id=user_id, session_id=session_id, final_profession=prof
        ).first()

        if record:
            record.score += score
        else:
            new_record = UserTestRecord(
                user_id=user_id,
                session_id=session_id,
                question_id=question_id,
                answer_id=answer.id,
                final_profession=prof,
                score=score
            )
            session.add(new_record)

    session.commit()
    session.close()
    return {"next_question": True}
