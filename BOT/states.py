from aiogram.filters.state import State, StatesGroup

class RegState(StatesGroup):
    waiting_for_password = State()
