
from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from BOT.states import RegState
from BOT.imports.db.database import init_db

con, cur = init_db()

router = Router()

@router.message(RegState.waiting_for_password)
async def save_password(message: types.Message, state: FSMContext):
    cur.execute(
        "INSERT INTO messages (user_id, username, text) VALUES (?, ?, ?)",
        (message.from_user.id, message.from_user.username, message.text)
    )
    con.commit()
    await message.answer("REGISTATIUA!")
    await state.clear()