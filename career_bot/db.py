from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Инициализация базы данных и базового класса для моделей
DATABASE_URL = 'sqlite:///akinator_bot.db'  # На этапе разработки используем SQLite
Base = declarative_base()
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# Модель для профессий
class Profession(Base):
    __tablename__ = 'professions'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    specialty = Column(String)
    category = Column(String)
    description = Column(String)
    skills = Column(String)
    technologies = Column(String)
    recommendations = Column(String)

# Модель для вопросов теста
class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)

    # Связь с ответами
    answers = relationship("Answer", back_populates="question")

# Модель для ответов на вопросы
class Answer(Base):
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('questions.id'))
    text = Column(String)
    professions_scores = Column(String)
    short_answer = Column(String)  # Новый столбец для кратких ответов, например, "A", "B", "C", "D"

    question = relationship("Question", back_populates="answers")

# Модель для записи данных о прохождении теста пользователем
class UserTestRecord(Base):
    __tablename__ = 'user_test_records'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    user_name = Column(String)
    question_id = Column(Integer, ForeignKey('questions.id'))
    answer_id = Column(Integer, ForeignKey('answers.id'))
    final_profession = Column(String)
    session_id = Column(String)  # Новый столбец для идентификатора сессии
    score = Column(Float)        # Новый столбец для баллов

# Создание всех таблиц в базе данных
Base.metadata.create_all(engine)
