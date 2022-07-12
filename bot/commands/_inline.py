from telegram import Update, InlineQueryResultCachedSticker
from telegram.ext import InlineQueryHandler, ContextTypes

from .. import database


async def inline_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    if query == "":
        await update.inline_query.answer([])

    result = database.search(query)
    await update.inline_query.answer([
        InlineQueryResultCachedSticker(sticker_id, file_id)
        for (sticker_id, file_id) in result
    ], auto_pagination=False)


inline_handler = InlineQueryHandler(inline_callback, block=False)
