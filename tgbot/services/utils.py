from aiogram import Bot
from aiogram.utils.markdown import hbold, hcode

from typing import Union
from asyncio import sleep

import requests

from tgbot.config import Config
from tgbot.keyboards import inline


def get_new_orders(kabanchik_auth: str) -> Union[list[dict], bool]:
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': (
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/117.0.0.0 Safari/537.36'
        ),
    }

    cookies = {
        'auth': kabanchik_auth
    }

    try:
        r = requests.get(
            'https://kabanchik.ua/ua/cabinet/recommended?page=1&category=92',
            cookies=cookies,
            headers=headers
        )

        if r.status_code != 200:
            return False

        else:
            return r.json().get('items')

    except Exception as e:
        print(e)
        return False


def get_unique_orders(orders: list[dict]) -> list[dict]:
    result = []

    with open('data/orders.txt', 'r+') as file:
        old_orders = file.read().split('\n')
        for order in orders:
            if str(order.get('id')) not in old_orders:
                result.append(order)
                file.write(f'{order.get('id')}\n')

    return result


async def parser(bot: Bot, config: Config):
    orders = get_new_orders(config.misc.kabanchik_auth)

    if orders:
        orders = get_unique_orders(orders)

        for order in orders:
            for user_id in config.tg_bot.admin_ids:
                await bot.send_message(
                    chat_id=user_id,
                    text=f'{hbold(order.get('title'))}\n\n'
                    f'💰 Сумма: {hcode(order.get('cost'))} грн\n\n'
                    f'🐷 Челикс: {hcode(order.get('customer').get('name'))}\n\n'
                    f'⏳ Выполнить до: {hcode(order.get('datetime_due').lower())}',
                    reply_markup=inline.get_url_button(order.get('url').strip()),
                    disable_web_page_preview=True
                )

                await sleep(0.05)
