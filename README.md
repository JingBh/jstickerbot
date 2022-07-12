# jstickerbot

A Telegram bot that allows you to search stickers by keywords.

> The bot is quite simple for now and is intended for my personal use only. Uptime and stability is not guaranteed.
> Contribute to the bot and its database if you want to use it too.

## Usage

The bot works in inline mode. When chatting with someone, you can simply type `@jstickerbot <keyword>` and the bot will
search for stickers with the keyword for you.

The keywords of a sticker should be predefined by the author of the sticker pack. Currently, the only way to achieve
this is by contributing to [the data repo](https://github.com/JingBh/jstickerbot_data) of the bot in GitHub.

## Contributing

To contribute to the data repo, you can take the `json` files in the data repo as examples. To be specific, the file
name is the ID of the sticker pack, while the keys is the `unique_file_id` of the sticker, which can be acquired by
sending stickers to the bot in debug mode.

Note that keywords can contain special characters, but cannot contain spaces.
