from career_bot.db import Session, Profession, UserTestRecord
from sqlalchemy import func

def calculate_result(user_id, session_id):
    session = Session()

    result = (
        session.query(
            Profession.name,
            Profession.description,
            Profession.skills,
            Profession.technologies,
            Profession.recommendations
        )
        .join(UserTestRecord, UserTestRecord.final_profession == Profession.name)
        .filter(UserTestRecord.user_id == user_id, UserTestRecord.session_id == session_id)
        .group_by(Profession.name)
        .order_by(func.sum(UserTestRecord.score).desc())
        .first()
    )

    session.close()

    if result:
        name, description, skills, technologies, recommendations = result
        result_text = (f"Вам подходит профессия: {name}\n\n"
                       f"Описание: {description}\n\n"
                       f"Требуемые навыки: {skills}\n\n"
                       f"Необходимые технологии: {technologies}\n\n"
                       f"Рекомендации: {recommendations}")
        return result_text
    else:
        return "Не удалось определить подходящую профессию."