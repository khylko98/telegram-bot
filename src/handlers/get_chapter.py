from telegram import Update
from telegram.ext import ContextTypes

from logging_config import setup_logger

from message_texts import GET_CHAPTER_INVALID, GET_CHAPTER_FAILED

from services.chapters import get_chapter_by_title


logger = setup_logger()


async def get_chapter(update: Update, context: ContextTypes.DEFAULT_TYPE):
    effective_chat = update.effective_chat
    if not effective_chat:
        logger.warning("effective_chat in None")
        return

    command_parts = update.message.text.split(" ")
    if len(command_parts) < 2:
        await context.bot.send_message(
            chat_id=effective_chat.id,
            text=GET_CHAPTER_INVALID,
        )
        return

    title = " ".join(command_parts[1:])
    chapter = get_chapter_by_title(title)
    if chapter:
        await context.bot.send_message(
            chat_id=effective_chat.id,
            text=f"Chapter found:\n id: {chapter.id},\n title: {chapter.title},\n audio_link: {chapter.audio_link}",
        )
    else:
        await context.bot.send_message(
            chat_id=effective_chat.id,
            text=GET_CHAPTER_FAILED,
        )
