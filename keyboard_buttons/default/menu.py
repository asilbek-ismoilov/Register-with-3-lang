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

def tel_buttons(language):
    button_texts = texts[language]["menu"]

    tel = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=button_texts["tel"], request_contact=True)]
        ],
        resize_keyboard=True,
        input_field_placeholder=button_texts["tel_text"]
    )

    return tel

def back_button(language):
    button_texts = texts[language]["menu"]

    back_button = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=button_texts["back"]),]
        ],
        resize_keyboard=True,
    )

    return back_button

menu_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Biz haqimizda 👥"),KeyboardButton(text="Manzilimiz 📍")],
        [KeyboardButton(text="Kurslar 📚"), KeyboardButton(text="Savol❓ va Takliflar 📝")]
    ],
    resize_keyboard=True,
)