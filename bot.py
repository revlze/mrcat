import asyncio
import logging
import os
import httpx
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import Message

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

CAT_API_KEY = os.environ["CAT_API_KEY"]
TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]

CAT_API_URL = "https://api.thecatapi.com/v1/images/search"

router = Router()


async def get_cat_image() -> str:
    async with httpx.AsyncClient() as client:
        response = await client.get(CAT_API_URL, headers={"x-api-key": CAT_API_KEY})
        response.raise_for_status()
        return response.json()[0]["url"]


@router.message(Command("start"))
async def start(message: Message):
    logger.info("start from chat_id=%s chat_type=%s", message.chat.id, message.chat.type)
    await message.answer("write /cat to get a random cat image!")


@router.message(Command("cat"))
async def cat(message: Message):
    logger.info("cat from chat_id=%s chat_type=%s", message.chat.id, message.chat.type)
    try:
        url = await get_cat_image()
        await message.answer_photo(url)
        logger.info("sent photo to chat_id=%s", message.chat.id)
    except Exception:
        logger.exception("failed to handle /cat in chat_id=%s", message.chat.id)
        raise


@router.message()
async def log_unhandled(message: Message):
    logger.info(
        "unhandled message chat_id=%s chat_type=%s text=%r",
        message.chat.id,
        message.chat.type,
        message.text,
    )


async def main():
    bot = Bot(token=TELEGRAM_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
