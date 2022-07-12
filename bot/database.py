import asyncio
import json
import logging
import os
from os.path import dirname, join, realpath
from typing import List, Tuple, Dict, Union, Sequence

from telegram import Bot

data: List[Dict[str, Union[str, Sequence[str]]]] = []


def initialize(bot: Bot):
    global data

    data = []
    data_dir = realpath(join(dirname(dirname(__file__)), 'data'))
    for walk in os.walk(data_dir):
        for file in walk[2]:
            if not file.endswith('.json') or file.startswith('.'):
                continue

            pack = file.split('.')[0]
            logging.info(f'Processing sticker pack {pack}')

            file_handle = open(join(walk[0], file), 'r', encoding='utf-8')
            keywords_data: Dict[str, List[str]] = json.loads(file_handle.read())

            loop = asyncio.get_event_loop()
            stickers = loop.run_until_complete(bot.get_sticker_set(pack)).stickers
            for sticker in stickers:
                if sticker.file_unique_id not in keywords_data:
                    continue

                data.append({
                    'id': sticker.file_unique_id,
                    'file_id': sticker.file_id,
                    'keywords': [
                        keyword.lower()
                        for keyword in keywords_data[sticker.file_unique_id]
                    ]
                })


def search(keywords: Union[str, List[str]]) -> Sequence[Tuple[str, str]]:
    if isinstance(keywords, str):
        keywords = keywords.split(' ')
    keywords = [keyword.lower().strip() for keyword in keywords]

    count = 0
    exact_matches: List[Tuple[str, str]] = []
    partial_matches: List[Tuple[str, str]] = []

    for sticker in data:
        is_match = True
        is_exact = True

        for keyword_input in keywords:
            if not is_match:
                break
            if keyword_input in sticker['keywords']:
                continue
            is_exact = False
            for keyword in sticker['keywords']:
                if keyword_input in keyword:
                    break
            else:
                is_match = False

        if is_match:
            count += 1
            sticker_result = (sticker['id'], sticker['file_id'])
            if is_exact:
                exact_matches.append(sticker_result)
            else:
                partial_matches.append(sticker_result)

            if count >= 50:
                break

    return exact_matches + partial_matches
