
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from BOT.states import RegState

router = Router()

@router.message(Command("reg"))
async def reg(message: types.Message, state: FSMContext):
    await message.answer("NAPISHI CHURKA")
    await state.set_state(RegState.waiting_for_password)
