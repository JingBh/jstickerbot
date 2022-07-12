from telegram import Update
from telegram.ext import MessageHandler
from telegram.ext.filters import Sticker


async def sticker_callback(update: Update, _):
    pack = update.effective_message.sticker.set_name
    pack_url = f'https://t.me/addstickers/{pack}'
    file_id = update.effective_message.sticker.file_unique_id
    await update.effective_message.reply_html(f'Sticker ID: <code>{file_id}</code>\n'
                                              f'From pack: {pack_url}',
                                              quote=True)


# Blocking here to reply messages one by one
sticker_handler = MessageHandler(Sticker.ALL, sticker_callback)
