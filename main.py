import os
import asyncio

from dotenv import load_dotenv
import telegram

from ztcodewars.codewars import get_stats



load_dotenv()

BOT_TOKEN = os.getenv("BOT_API_KEY")


async def handle_updates(updates, bot: telegram.Bot):
    for u in updates:
        chat_id = u.message.chat.id
        username = u.message.text
        text = get_stats(username)
        await bot.send_message(chat_id, text)

async def main():
    bot = telegram.Bot(BOT_TOKEN)
    async with bot:
        updates = await bot.get_updates()
        await handle_updates(updates, bot)


if __name__ == "__main__":
    asyncio.run(main())
