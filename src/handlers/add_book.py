from telegram import Update
from telegram.ext import ContextTypes

from logging_config import setup_logger
from message_texts import ADD_BOOK_INVALID, ADD_BOOK_SUCCES, ADD_BOOK_FAILED

from services.books import insert_book


logger = setup_logger()


async def add_book(update: Update, context: ContextTypes.DEFAULT_TYPE):
    effective_chat = update.effective_chat
    if not effective_chat:
        logger.warning("effective_chat in None")
        return

    command_parts = update.message.text.split(" ")
    if len(command_parts) < 4:
        await context.bot.send_message(
            chat_id=effective_chat.id,
            text=ADD_BOOK_INVALID,
        )
        return

    title = " ".join(command_parts[1:-2])
    img_link = command_parts[-2]
    bg_img_link = command_parts[-1]
    if insert_book(title, img_link, bg_img_link):
        await context.bot.send_message(
            chat_id=effective_chat.id,
            text=ADD_BOOK_SUCCES,
        )
    else:
        await context.bot.send_message(
            chat_id=effective_chat.id,
            text=ADD_BOOK_FAILED,
        )
