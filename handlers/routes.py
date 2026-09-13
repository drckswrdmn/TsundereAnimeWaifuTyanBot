from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from random import choice
import asyncio
from aiogram import Bot, types
from phrases import *
from handlers.client import client

router = Router()

subscribers = set()

async def notifier(bot: Bot):
    while True:
        if subscribers:
            for user_id in list(subscribers):
                try:
                    Hello = choice(choice(tsundere_first_meet))
                    await bot.send_message(user_id, Hello)
                except Exception:
                    pass

        await asyncio.sleep(86400)

@router.message(Command('start'))
async def start(message: Message):
    await message.answer(choice(tsundere_first_meet))

@router.message(Command('subscribe'))
async def subscribe(message: Message):
    user_id = message.from_user.id

    subscribers.add(user_id)

    await message.answer(tsundere_subscribe)

@router.message(Command('unsubscribe'))
async def unsubscribe(message: Message):
    user_id = message.from_user.id

    subscribers.discard(user_id)

    await message.answer(tsundere_unsubscribe)

@router.message(Command('showsubscribers'))
async def showsubscribers(message: Message):
    if not subscribers:
        await message.answer(tsundere_none_subscribers)
        return
    text = "Подписчики:\n"
    for uid in subscribers:
        text += f"{uid}\n"
    await message.answer(text)

@router.message(F.text)
async def chat(message: types.Message):
    user_text = message.text

    await message.bot.send_chat_action(message.chat.id, "typing")

    try:
        response = client.responses.create(
            model="GPT-OSS-120B",
            input=[
                {"role": "system", "content": "Ты должна отвечать в стилистике аниме-девочки-цундэре и добавлять один-два стикера, отборажающие твои эмоции"},
                {"role": "user", "content": user_text}
            ],
            max_output_tokens=750
        )

        await message.answer(response.output_text)

    except Exception as e:
        print("TsundereAI error:", e)
        await message.answer("Прости, зайчик, не могу тебе ответить, что-то с интернетом")

