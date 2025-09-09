
from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name} напиши /reg чтобы ввести пароль и ты будешь в бд")
    