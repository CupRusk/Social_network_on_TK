import asyncio
from BOT.imports.imports import init_aiogram_bot
from BOT.imports.db.database import init_db
from BOT.routers.start import router as start_router
from BOT.routers.reg import router as reg_router
from BOT.routers.wait_the_pass import router as wait_the_pass_router


def init_bot(Token):
    print("Бот активирован!")

    API_TOKEN = "8080089791:AAFH72zdQJIj1jP75ka0nEgJKHG1TaWYi_M"  # лучше вынести в .env

    # Инициализация бота и базы
    bot, dp, _ = init_aiogram_bot(API_TOKEN)
    con, cur = init_db()

    # Подключаем роутеры
    dp.include_router(start_router)
    dp.include_router(reg_router)
    dp.include_router(wait_the_pass_router)

    async def main():
        await dp.start_polling(bot)

    # Запуск асинхронного цикла
    asyncio.run(main())
