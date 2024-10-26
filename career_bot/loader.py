from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage  # Импортируем MemoryStorage для хранения состояний
from config import BOT_TOKEN

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()  # Создаём экземпляр MemoryStorage
dp = Dispatcher(bot, storage=storage)  # Передаем storage диспетчеру
