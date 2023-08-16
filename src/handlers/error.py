from telegram import Update
from telegram.ext import ContextTypes

from logging_config import setup_logger


logger = setup_logger()


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f"Update {update} caused error {context.error}")
