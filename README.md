# RUSSIAN VERSION

# Telegram Roulette Bot 🎰

Простой Telegram-бот с игрой в рулетку, реализованный на Python с использованием библиотеки `aiogram`. Бот использует `SQLite` для хранения данных о пользователях и их попытках.

## ✨ Возможности

-   **Система рулетки**: Пользователи могут крутить рулетку, чтобы выиграть случайный приз.
-   **Система попыток**: Каждый пользователь имеет ограниченное количество попыток (по умолчанию 3).
-   **База данных**: Используется SQLite для надежного хранения данных.
-   **Админ-панель**: Администратор может добавлять попытки любому пользователю с помощью специальной команды.
-   **Инлайн-кнопки**: Удобный интерфейс с кнопкой "Крутить".

## 🛠️ Установка и запуск

1.  **Клонируйте репозиторий:**
    ```bash
    git clone [https://github.com/your-username/telegram-roulette-bot.git](https://github.com/your-username/telegram-roulette-bot.git)
    cd telegram-roulette-bot
    ```

2.  **Установите зависимости:**
    Рекомендуется использовать виртуальное окружение.
    ```bash
    pip install aiogram
    ```

3.  **Настройте конфигурацию:**
    -   Откройте файл `telegram_bot/cfg.py`.
    -   Вставьте токен вашего бота в переменную `BOT_TOKEN`. Вы можете получить его у [@BotFather](https://t.me/BotFather).
    -   Укажите свой Telegram User ID в переменной `ADMIN_ID`. Вы можете узнать его у [@userinfobot](https://t.me/userinfobot).

4.  **Запустите бота:**
    ```bash
    python telegram_bot/main.py
    ```

## ⚙️ Как пользоваться

-   **/start**: Начать взаимодействие с ботом, получить приветственное сообщение и клавиатуру для игры.
-   **Кнопка "Крутить рулетку!"**: Нажмите, чтобы потратить одну попытку и получить случайный приз.
-   **/add_attempts \[user_id] \[количество]**: (Только для админа) Добавляет указанное количество попыток пользователю с заданным `user_id`.

## ✏️ Кастомизация

Этот бот создан как легко редактируемая основа. Вы можете легко изменить:
-   **Список призов**: Отредактируйте список `PRIZES` в файле `main.py`.
-   **Количество попыток по умолчанию**: Измените значение `DEFAULT 3` в `db.py`.
-   **Тексты сообщений**: Все тексты находятся в `main.py` и могут быть легко изменены.

---
---
---

# ENGLISH VERSION

# Telegram Roulette Bot 🎰

A simple Telegram bot with a roulette game, implemented in Python using the `aiogram` library. The bot uses `SQLite` to store data about users and their attempts.

## ✨ Features

-   **Roulette System**: Users can spin the roulette to win a random prize.
-   **Attempt System**: Each user has a limited number of attempts (default is 3).
-   **Database**: Uses SQLite for reliable data storage.
-   **Admin Panel**: An administrator can add attempts to any user with a special command.
-   **Inline Buttons**: A user-friendly interface with a "Spin" button.

## 🛠️ Installation and Launch

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/telegram-roulette-bot.git](https://github.com/your-username/telegram-roulette-bot.git)
    cd telegram-roulette-bot
    ```

2.  **Install dependencies:**
    It is recommended to use a virtual environment.
    ```bash
    pip install aiogram
    ```

3.  **Configure the settings:**
    -   Open the `telegram_bot/cfg.py` file.
    -   Insert your bot's token into the `BOT_TOKEN` variable. You can get it from [@BotFather](https://t.me/BotFather).
    -   Specify your Telegram User ID in the `ADMIN_ID` variable. You can find it by messaging [@userinfobot](https://t.me/userinfobot).

4.  **Launch the bot:**
    ```bash
    python telegram_bot/main.py
    ```

## ⚙️ How to Use

-   **/start**: Start interacting with the bot, receive a welcome message and the game keyboard.
-   **"Spin the roulette!" button**: Press to spend one attempt and get a random prize.
-   **/add_attempts \[user_id] \[amount]**: (Admin only) Adds the specified number of attempts to the user with the given `user_id`.

## ✏️ Customization

This bot is designed as an easily editable foundation. You can easily change:
-   **List of prizes**: Edit the `PRIZES` list in `main.py`.
-   **Default number of attempts**: Change the `DEFAULT 3` value in `db.py`.
-   **Message texts**: All texts are in `main.py` and can be easily modified.
