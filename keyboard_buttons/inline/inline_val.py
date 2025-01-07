from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

language = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text= "O'zbek 🇺🇿", callback_data="uz"),
        InlineKeyboardButton(text= "English 🇺🇸", callback_data="us"),
        InlineKeyboardButton(text= "Русский 🇷🇺", callback_data="ru")
        ]
    ]
)

import json

def load_buttons():
    with open("languages.json", "r", encoding="utf-8") as f:
        return json.load(f)

texts = load_buttons()

def create_inline_buttons(language):
    button_text = texts[language]["menu"]["inline_button"]

    inline_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=button_text, callback_data="reg_cours")]
        ]
    )
    return inline_keyboard

def confirmation_buttons(language):
    button_text = texts[language]["menu"]

    confirmation = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=button_text["cancel"], callback_data="cancel"), InlineKeyboardButton(text=button_text["change"], callback_data="change"), InlineKeyboardButton(text=button_text["right"], callback_data="right")]
        ]
    )
    return confirmation
