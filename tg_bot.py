import asyncio
import sqlite3
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage  
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup
from aiogram.filters import Command 
from aiogram import Router

API_TOKEN = ""


bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage()) 
router = Router() 


con = sqlite3.connect("bot.db.sql")
cur = con.cursor()
cur.execute(
    '''
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        username text,
        text NOT NULL
    
    )
    
    
    
    '''
)
con.commit()    

class RegState(StatesGroup):
    waiting_for_password = State()

@router.message(Command("start"))
async def start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name} напиши /reg чтобы ввести пароль и ты будешь в бд")
    
@router.message(Command("reg"))
async def reg(message: types.Message, state: FSMContext):
    await message.answer("NAPISHI CHURKA")
    await state.set_state(RegState.waiting_for_password)


@router.message(RegState.waiting_for_password)
async def save_password(message: types.Message, state: FSMContext):
    cur.execute(
        "INSERT INTO messages (user_id, username, text) VALUES (?, ?, ?)",
        (message.from_user.id, message.from_user.username, message.text)
    )
    con.commit()
    await message.answer("REGISTATIUA!")
    await state.clear()
    
    
dp.include_router(router)    
    
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
