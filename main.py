from os import getenv
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers.routes import router, notifier
from openai import OpenAI

load_dotenv()
TOKEN = getenv("BOT_TOKEN")
AIKEY = getenv("AI_KEY")

dp = Dispatcher()
dp.include_router(router)

client = OpenAI(api_key=AIKEY, base_url="https://speshu.ai/api/v1")

async def main():
    bot = Bot(token=TOKEN)

    asyncio.create_task(notifier(bot))

    print("TsundereTyan is working...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())