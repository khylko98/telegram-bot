import config, handlers

from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

from logging_config import setup_logger


COMMAND_HANDLERS = {
    "start": handlers.start,
    "help": handlers.help,
    "add_book": handlers.add_book,
    "get_book": handlers.get_book,
    "get_chapter": handlers.get_chapter,
}

logger = setup_logger()

if not config.TELEGRAM_BOT_TOKEN or not config.TELEGRAM_BOT_USERNAME:
    raise ValueError(
        "TELEGRAM_BOT_TOKEN and TELEGRAM_BOT_USERNAME env variables "
        "wasn't implemented in .env (both should be initialized)."
    )


def main():
    app = ApplicationBuilder().token(config.TELEGRAM_BOT_TOKEN).build()

    for command_name, command_handler in COMMAND_HANDLERS.items():
        app.add_handler(CommandHandler(command_name, command_handler))

    add_chapter_handler = MessageHandler(filters.AUDIO, handlers.add_chapter)
    app.add_handler(add_chapter_handler)

    app.add_error_handler(handlers.error)

    app.run_polling()


if __name__ == "__main__":
    try:
        main()
    except Exception:
        import traceback

        logger.warning(traceback.format_exc())
