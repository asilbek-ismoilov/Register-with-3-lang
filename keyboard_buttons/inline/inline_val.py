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

inline_button_uz = create_inline_buttons("uz")
inline_button_us = create_inline_buttons("us")
inline_button_ru = create_inline_buttons("ru")

confirmation = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text= "Bekor qilish ❌", callback_data="cancel"), InlineKeyboardButton(text= "O'zgartirish 📝", callback_data="change"), InlineKeyboardButton(text= "Tasdiqlash ✅", callback_data="right")]
    ]
)
