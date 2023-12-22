import asyncio
from openai import OpenAI

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

TOKEN = "6451493735:AAEWAwXKxnkhszjaIaTR7pDHdDLVrmyr73Y"
CHATGPT_TOKEN = "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"

dp = Dispatcher()
client = OpenAI(api_key=CHATGPT_TOKEN)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f'Эта хуйня работает, {message.from_user.full_name}')


@dp.message()
async def any_message_handler(message: Message) -> None:
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'user', 'content': message.text}
        ]
    )
    print(response.choices[0].message.content)
    await message.answer(response.choices[0].message.content)


async def main() -> None:
    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
