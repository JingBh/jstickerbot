import json

from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, ContextTypes
from telegram.ext.filters import Sticker, TEXT, COMMAND, ChatType


async def sticker_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pack = update.effective_message.sticker.set_name
    pack_url = f'https://t.me/addstickers/{pack}'
    file_id = update.effective_message.sticker.file_unique_id

    context.user_data['editing_sticker'] = file_id

    await update.effective_message.reply_html(f'Sticker ID: <code>{file_id}</code>\n'
                                              f'From pack: {pack_url}',
                                              quote=True)


# Blocking here to reply messages one by one
sticker_handler = MessageHandler(Sticker.ALL & ChatType.PRIVATE, sticker_callback)


async def sticker_tagging_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    stickers = context.user_data.get('editing_stickers', {})
    sticker_id = context.user_data.get('editing_sticker')
    if sticker_id is not None:
        stickers[sticker_id] = [i.strip() for i in update.effective_message.text.split(' ')]
        del context.user_data['editing_sticker']
    context.user_data['editing_stickers'] = stickers
    await update.effective_message.reply_text('OK')


sticker_tagging_handler = MessageHandler(TEXT & ~COMMAND & ChatType.PRIVATE, sticker_tagging_callback)


async def sticker_tagging_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    stickers = context.user_data.get('editing_stickers', {})
    code = json.dumps(stickers, indent=2, ensure_ascii=False)
    await update.effective_message.reply_html(f'<code>{code}</code>')


sticker_tagging_get_handler = CommandHandler('edited', sticker_tagging_command, ChatType.PRIVATE)
