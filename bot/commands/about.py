from telegram import Update
from telegram.ext import CommandHandler


async def about_command(update: Update, _):
    await update.message.reply_text('I am a work of @JingBh.\n'
                                    'You can also view my source here: '
                                    'https://github.com/JingBh/jstickerbot')


about_handler = CommandHandler('about', about_command, block=False)
