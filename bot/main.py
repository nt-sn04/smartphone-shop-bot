from telegram.ext import (
    Updater,
)

from bot.config import settings


def main():
    updater = Updater(settings.BOT_TOKEN)
    dp = updater.dispatcher

    updater.start_polling()
    updater.idle()
