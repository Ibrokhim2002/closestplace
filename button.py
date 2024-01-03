import json
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton




def create_user_location(language, messages):
    user_location = ReplyKeyboardMarkup(resize_keyboard=True)
    user_location.add(KeyboardButton(messages[int(language[-1][-1])][language]["user_location"], request_location=True))
    return user_location

def create_buttons_column1(language, messages):
    buttons_column1 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(messages[int(language[-1][-1])][language]["buttons_column1"][0][0], callback_data='airport'),
                InlineKeyboardButton(messages[int(language[-1][-1])][language]["buttons_column1"][0][1], callback_data='supermarket'),
            ],
            [
                InlineKeyboardButton(messages[int(language[-1][-1])][language]["buttons_column1"][1][0], callback_data='bank'),
                InlineKeyboardButton(messages[int(language[-1][-1])][language]["buttons_column1"][1][1], callback_data='hospital'),
            ],
            [
                InlineKeyboardButton(messages[int(language[-1][-1])][language]["buttons_column1"][2][0], callback_data='mosque'),
                InlineKeyboardButton(messages[int(language[-1][-1])][language]["buttons_column1"][2][1], callback_data='restaurant'),
            ],
            [
                InlineKeyboardButton(messages[int(language[-1][-1])][language]["buttons_column1"][3][0], callback_data='bus_station'),
                InlineKeyboardButton(messages[int(language[-1][-1])][language]["buttons_column1"][3][1], callback_data='subway_station'),
            ],
            [
                InlineKeyboardButton(messages[int(language[-1][-1])][language]["buttons_column1"][4][0], callback_data='gas_station'),
                InlineKeyboardButton(messages[int(language[-1][-1])][language]["buttons_column1"][4][1], callback_data='pharmacy'),
            ],
            [
                InlineKeyboardButton(messages[int(language[-1][-1])][language]["buttons_column1"][5][0], callback_data='amusement_park'),
                InlineKeyboardButton(messages[int(language[-1][-1])][language]["buttons_column1"][5][1], callback_data='car_wash'),
            ],
            [
                InlineKeyboardButton(messages[int(language[-1][-1])][language]["buttons_column1"][6][0], callback_data='type_yourself'),
            ],
        ]
    )
    return buttons_column1

def language_user(language, messages):
    user_location = create_user_location(language, messages)
    buttons_column1 = create_buttons_column1(language, messages)

    more1 = InlineKeyboardMarkup(row_width=1)
    more_button = InlineKeyboardButton(messages[int(language[-1][-1])][language]["more_button"], callback_data="more")
    more1.add(more_button)

    return user_location, buttons_column1, more1
    s


buttons_column2 = InlineKeyboardMarkup(row_width=3)
buttons_column2.add(
    InlineKeyboardButton("🇺🇿 Uzbek", callback_data="uz1"),
    InlineKeyboardButton("🇷🇺 Russian", callback_data="ru2"),
    InlineKeyboardButton("🇬🇧 English", callback_data="en0")
)