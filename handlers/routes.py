from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from random import choice
import asyncio
from aiogram import Bot
from phrases import *

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

        await asyncio.sleep(10)


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