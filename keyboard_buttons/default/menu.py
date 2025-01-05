from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import json

def load_buttons():
    with open("languages.json", "r", encoding="utf-8") as f:
        return json.load(f)

texts = load_buttons()

def create_menu_buttons(language):
    button_texts = texts[language]["menu"]

    menu_buttons = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=button_texts["menu_button_1"]), KeyboardButton(text=button_texts["menu_button_3"])],
            [KeyboardButton(text=button_texts["menu_button_2"]),KeyboardButton(text=button_texts["menu_button_5"]),  KeyboardButton(text=button_texts["menu_button_4"])]
        ],
        resize_keyboard=True,
    )
    return menu_buttons

menu_button_uz = create_menu_buttons("uz")
menu_button_us = create_menu_buttons("us")
menu_button_ru = create_menu_buttons("ru")

def course_buttons(language):
    button_texts = texts[language]["menu"]

    course_buttons = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Python"), KeyboardButton(text="SMM")],
            [KeyboardButton(text=button_texts["back"])]
        ],
        resize_keyboard=True,
    )
    return course_buttons

course_button_uz = course_buttons("uz")
course_button_us = course_buttons("us")
course_button_ru = course_buttons("ru")

tel = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Telefon raqam yuborish ☎️', request_contact=True)]
    ],
    resize_keyboard=True
)

menu_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Biz haqimizda 👥"),KeyboardButton(text="Manzilimiz 📍")],
        [KeyboardButton(text="Kurslar 📚"), KeyboardButton(text="Savol❓ va Takliflar 📝")]
    ],
    resize_keyboard=True,
)

back_about = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔙Orqaga"),]
    ],
    resize_keyboard=True,
)