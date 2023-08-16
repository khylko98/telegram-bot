from telegram import Update
from telegram.ext import ContextTypes

from logging_config import setup_logger

from message_texts import ADD_CHAPTER_NO_AUDIO, ADD_CHAPTER_SUCCES, ADD_CHAPTER_FAILED

from services.chapters import insert_chapter


logger = setup_logger()


async def add_chapter(update: Update, context: ContextTypes.DEFAULT_TYPE):
    effective_chat = update.effective_chat
    if not effective_chat:
        logger.warning("effective_chat in None")
        return

    if not update.message.audio:
        await context.bot.send_message(
            chat_id=effective_chat.id,
            text=ADD_CHAPTER_NO_AUDIO,
        )
        return

    file_id = update.message.audio.file_id
    file_name = update.message.audio.file_name
    file_info = await context.bot.get_file(file_id)
    file_path = file_info.file_path

    title = file_name[2:-4]
    book_id = file_name[0]
    if insert_chapter(book_id, title, file_path):
        await context.bot.send_message(
            chat_id=effective_chat.id,
            text=ADD_CHAPTER_SUCCES,
        )
    else:
        await context.bot.send_message(
            chat_id=effective_chat.id,
            text=ADD_CHAPTER_FAILED,
        )
