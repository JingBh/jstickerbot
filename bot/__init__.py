from telegram.ext import ApplicationBuilder

from . import config, setup_logging, commands, database

application = ApplicationBuilder() \
    .token(config.token) \
    .build()

commands.register(application)
database.initialize(application.bot)


def start():
    application.run_polling()
