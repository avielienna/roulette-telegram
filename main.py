# /telegram_bot/main.py (ВЕРСИЯ ДЛЯ AIOGRAM 3.x)

import asyncio
import logging
import random
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command, CommandObject
from aiogram.fsm.storage.memory import MemoryStorage
import cfg
import db
import handlerkeyboard as kb


logging.basicConfig(level=logging.INFO)
dp = Dispatcher(storage=MemoryStorage())

PRIZES = ["🍏", "🍊", "🍋", "🍌", "🍉", "🍇", "🍓", "🍒", "🍑", "🍍"]

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    db.add_user_if_not_exists(user_id)
    
    attempts = db.get_attempts(user_id)
    text = (f"🎉 Привет, это бот-рулетка!\n\n"
            f"Испытай свою удачу. У тебя есть *{attempts}* попыток.\n\n"
            f"Жми на кнопку, чтобы начать!")

    await message.answer(text, reply_markup=kb.get_roulette_keyboard(), parse_mode="Markdown")

@dp.message(Command("add_attempts"))
async def cmd_add_attempts(message: types.Message, command: CommandObject, bot: Bot):
    if message.from_user.id != cfg.ADMIN_ID:
        return

    try:
        args = command.args.split()
        if len(args) != 2:
            await message.reply("Ошибка. Формат: /add_attempts [ID пользователя] [число]")
            return

        user_id_to_add, amount = map(int, args)
        
        current_attempts = db.get_attempts(user_id_to_add)
        new_attempts = current_attempts + amount
        db.update_attempts(user_id_to_add, new_attempts)

        await message.reply(f"✅ Готово! Добавил {amount} попыток юзеру {user_id_to_add}. "
                            f"Теперь у него {new_attempts}.")
        
        try:
            await bot.send_message(user_id_to_add, f"🎉 Администратор начислил вам *{amount}* попыток!", parse_mode="Markdown")
        except Exception:
            await message.reply("(Не удалось уведомить пользователя)")

    except (ValueError, IndexError, TypeError):
        await message.reply("ID пользователя и количество должны быть числами. Проверьте формат.")

@dp.callback_query(F.data == "spin_roulette")
async def cb_spin_roulette(call: types.CallbackQuery):
    user_id = call.from_user.id
    attempts_left = db.get_attempts(user_id)

    if attempts_left <= 0:
        await call.answer("Упс, попытки закончились!", show_alert=True)
        return

    attempts_left -= 1
    db.update_attempts(user_id, attempts_left)

    prize = random.choice(PRIZES)
    text = (f"Крутим... Выпал приз: *{prize}*!\n\n"
            f"Осталось попыток: *{attempts_left}*.")

    await call.message.edit_text(text, reply_markup=kb.get_roulette_keyboard(), parse_mode="Markdown")
    await call.answer()

async def main():
    bot = Bot(token=cfg.BOT_TOKEN)
    
    print("Инициализация базы данных...")
    db.init_db()
    print("База готова.")
    print("Бот запущен!")
    
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())