import asyncio
import os
from datetime import datetime, timedelta, timezone

from aiogram import Bot

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

# Time to send the daily reminder (UTC), format "HH:MM"
REMINDER_TIME = os.getenv("REMINDER_TIME", "09:00")
REMINDER_TEXT = os.getenv("REMINDER_TEXT", "🔔 Ежедневное напоминание!")

try:
    _hour, _minute = map(int, REMINDER_TIME.split(":"))
    if not (0 <= _hour <= 23 and 0 <= _minute <= 59):
        raise ValueError
except ValueError:
    raise SystemExit(f"Invalid REMINDER_TIME '{REMINDER_TIME}'. Expected format: HH:MM (e.g. 09:00)")


async def main() -> None:
    bot = Bot(token=BOT_TOKEN)

    while True:
        now = datetime.now(timezone.utc)
        target = now.replace(hour=_hour, minute=_minute, second=0, microsecond=0)
        if now >= target:
            target += timedelta(days=1)

        wait_seconds = (target - now).total_seconds()
        print(f"Next reminder at {target.strftime('%Y-%m-%d %H:%M')} UTC "
              f"(in {wait_seconds / 3600:.1f} hours)")
        await asyncio.sleep(wait_seconds)

        await bot.send_message(chat_id=CHAT_ID, text=REMINDER_TEXT)
        print(f"Reminder sent at {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')} UTC")


if __name__ == "__main__":
    asyncio.run(main())
