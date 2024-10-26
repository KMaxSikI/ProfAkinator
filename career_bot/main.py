from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage  # Импортируем MemoryStorage
from config import BOT_TOKEN
from handlers import start, test, result, error

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()  # Создаём экземпляр MemoryStorage
dp = Dispatcher(bot, storage=storage)  # Передаем storage диспетчеру

# Регистрируем хендлеры
start.register_handlers_start(dp)
test.register_handlers_test(dp)
result.register_handlers_result(dp)
error.register_handlers_errors(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
