from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardBuilder


def get_url_button(url: str):
    return InlineKeyboardBuilder().row(InlineKeyboardButton(text='Посмотреть на сайте🌍', url=url)).as_markup()
