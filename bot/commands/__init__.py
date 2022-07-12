from telegram.ext import Application

from ._inline import inline_handler
from ..config import is_debug
from .about import about_handler
from .start import start_handler
from ._sticker import sticker_handler
from ._error import error_handler


def register(application: Application):
    application.add_handler(start_handler)
    application.add_handler(about_handler)

    application.add_handler(inline_handler)

    if is_debug:
        application.add_handler(sticker_handler)
    else:
        application.add_error_handler(error_handler)
