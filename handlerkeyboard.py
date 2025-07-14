# /telegram_bot/handlerkeyboard.py

from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_roulette_keyboard():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="🎰 Крутить рулетку!",
        callback_data="spin_roulette"
    ))
    return builder.as_markup()