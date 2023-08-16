from telegram import Update
from telegram.ext import ContextTypes

from logging_config import setup_logger

from message_texts import HELP


logger = setup_logger()


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    effective_chat = update.effective_chat
    if not effective_chat:
        logger.warning("effective_chat in None")
        return

    await context.bot.send_message(chat_id=effective_chat.id, text=HELP)
