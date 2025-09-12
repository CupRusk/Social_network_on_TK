from aiogram import Bot
from aiogram.utils.token import TokenValidationError

def validate_token(token: str) -> bool:
    try:
        Bot(token=token)
        return True
    except TokenValidationError:
        return False