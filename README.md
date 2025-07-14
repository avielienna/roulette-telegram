# Telegram Roulette Bot 🎰

## 🇷🇺 Описание / 🇬🇧 Description

🇷🇺 Простой Telegram-бот с игрой в рулетку, реализованный на Python с использованием библиотеки aiogram. Бот использует SQLite для хранения данных о пользователях и их попытках.

🇬🇧 A simple Telegram bot with a roulette game, implemented in Python using the aiogram library. The bot uses SQLite to store data about users and their attempts.

---

## ✨ Возможности / ✨ Features

* **🇷🇺 Система рулетки:** Пользователи могут крутить рулетку, чтобы выиграть случайный приз.
* **🇬🇧 Roulette System:** Users can spin the roulette to win a random prize.

* **🇷🇺 Система попыток:** Каждый пользователь имеет ограниченное количество попыток (по умолчанию 3).
* **🇬🇧 Attempt System:** Each user has a limited number of attempts (default is 3).

* **🇷🇺 База данных:** Используется SQLite для надежного хранения данных.
* **🇬🇧 Data Storage:** Uses SQLite for reliable data storage.

* **🇷🇺 Админ-панель:** Администратор может добавлять попытки любому пользователю с помощью специальной команды.
* **🇬🇧 Admin Panel:** An administrator can add attempts to any user with a special command.

* **🇷🇺 Инлайн-кнопки:** Удобный интерфейс с кнопкой "Крутить".
* **🇬🇧 Inline Buttons:** A user-friendly interface with a "Spin" button.

---

## 🛠️ Установка и запуск / 🛠️ Installation and Launch

1.  **🇷🇺 Клонируйте репозиторий / 🇬🇧 Clone the repository:**
    ```bash
    git clone https://github.com/avielienna/roulette-telegram.git
    cd roulette-telegram
    ```

2.  **🇷🇺 Установите зависимости / 🇬🇧 Install dependencies:**
    *(Рекомендуется использовать виртуальное окружение / Virtual environment recommended)*
    ```bash
    pip install aiogram
    ```

3.  **🇷🇺 Настройте конфигурацию / 🇬🇧 Configure the settings:**
    Откройте файл `roulette-telegram/cfg.py`.
    * **🇷🇺 Токен бота:** Вставьте токен вашего бота в `BOT_TOKEN` (получите у [@BotFather](https://t.me/BotFather)).
    * **🇬🇧 Bot Token:** Insert your bot's token into the `BOT_TOKEN` variable (get it from @BotFather).
    * **🇷🇺 ID админа:** Укажите свой Telegram User ID в `ADMIN_ID` (узнайте у [@userinfobot](https://t.me/userinfobot)).
    * **🇬🇧 Admin ID:** Specify your Telegram User ID in the `ADMIN_ID` variable (find it by messaging @userinfobot).

4.  **🇷🇺 Запустите бота / 🇬🇧 Launch the bot:**
    ```bash
    python roulette-telegram/main.py
    ```

---

## ⚙️ Как пользоваться / ⚙️ How to Use

* **🇷🇺 /start:** Начать взаимодействие с ботом, получить приветственное сообщение и клавиатуру для игры.
* **🇬🇧 /start:** Start interacting with the bot, receive a welcome message and the game keyboard.

* **🇷🇺 Кнопка "Крутить рулетку!":** Нажмите, чтобы потратить одну попытку и получить случайный приз.
* **🇬🇧 "Spin the roulette!" button:** Press to spend one attempt and get a random prize.

* **🇷🇺 /add_attempts [user_id] [количество]:** (Только для админа) Добавляет указанное количество попыток пользователю с заданным `user_id`.
* **🇬🇧 /add_attempts [user_id] [amount]:** (Admin only) Adds the specified number of attempts to the user with the given `user_id`.

---

## ✏️ Кастомизация / ✏️ Customization

🇷🇺 Этот бот создан как легко редактируемая основа. Вы можете легко изменить:

🇬🇧 This bot is designed as an easily editable foundation. You can easily change:

* **🇷🇺 Список призов:** Отредактируйте список `PRIZES` в файле `main.py`.
* **🇬🇧 List of prizes:** Edit the `PRIZES` list in `main.py`.

* **🇷🇺 Количество попыток по умолчанию:** Измените значение `DEFAULT 3` в `db.py`.
* **🇬🇧 Default number of attempts:** Change the `DEFAULT 3` value in `db.py`.

* **🇷🇺 Тексты сообщений:** Все тексты находятся в `main.py` и могут быть легко изменены.
* **🇬🇧 Message texts:** All texts are in `main.py` and can be easily modified.
