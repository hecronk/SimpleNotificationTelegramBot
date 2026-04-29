# SimpleNotificationTelegramBot

Простой Telegram-бот на Python (aiogram 3), который каждый день отправляет вам напоминание.

## Установка

```bash
pip install -r requirements.txt
```

## Настройка

1. Скопируйте `.env.example` в `.env` и заполните переменные:

```bash
cp .env.example .env
```

| Переменная | Описание |
|------------|----------|
| `BOT_TOKEN` | Токен бота от [@BotFather](https://t.me/BotFather) |
| `CHAT_ID` | Ваш Telegram chat ID (узнать через [@userinfobot](https://t.me/userinfobot)) |
| `REMINDER_TIME` | Время отправки по Екатеринбургу (UTC+5), формат `HH:MM` (по умолчанию `09:00`) |
| `REMINDER_TEXT` | Текст напоминания (по умолчанию `🔔 Ежедневное напоминание!`) |

2. Экспортируйте переменные окружения:

```bash
export BOT_TOKEN=your_bot_token_here
export CHAT_ID=your_chat_id_here
export REMINDER_TIME=09:00
export REMINDER_TEXT="🔔 Не забудь про дела!"
```

## Запуск

```bash
python bot.py
```

Бот будет работать в фоне и каждый день в указанное время отправлять вам сообщение.