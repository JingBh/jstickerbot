from telegram import Update
from telegram.ext import CommandHandler
from telegram.ext.filters import ChatType


async def start_command(update: Update, _):
    # await update.message.reply_text('Send any sticker to me to allow me to '
    #                                 'search the sticker pack that it is from, '
    #                                 'then you will be able to use inline query '
    #                                 'in any chat to search for stickers.')
    await update.message.reply_text('Use inline query in any chat to search for stickers.')


# Respond to start command in pm only.
start_handler = CommandHandler('start', start_command, ChatType.PRIVATE, block=False)
