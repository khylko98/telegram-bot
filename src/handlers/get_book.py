from telegram import Update
from telegram.ext import ContextTypes

from logging_config import setup_logger

from message_texts import GET_BOOK_INVALID, GET_BOOK_FAILED

from services.books import get_book_by_title


logger = setup_logger()


async def get_book(update: Update, context: ContextTypes.DEFAULT_TYPE):
    effective_chat = update.effective_chat
    if not effective_chat:
        logger.warning("effective_chat in None")
        return

    command_parts = update.message.text.split(" ")
    if len(command_parts) < 2:
        await context.bot.send_message(
            chat_id=effective_chat.id,
            text=GET_BOOK_INVALID,
        )
        return

    title = " ".join(command_parts[1:])
    book = get_book_by_title(title)
    if book:
        await context.bot.send_message(
            chat_id=effective_chat.id,
            text=f"Book found:\n id: {book.id},\n title: {book.title},\n img_link: {book.img_link},\n bg_img_link: {book.bg_img_link}",
        )
    else:
        await context.bot.send_message(
            chat_id=effective_chat.id,
            text=GET_BOOK_FAILED,
        )
