from aiogram import Bot, Dispatcher, Router
from aiogram.fsm.storage.memory import MemoryStorage

def init_aiogram_bot(token: str):
    bot = Bot(token=token)
    dp = Dispatcher(storage=MemoryStorage())
    router = Router()
    dp.include_router(router)
    return bot, dp, router
