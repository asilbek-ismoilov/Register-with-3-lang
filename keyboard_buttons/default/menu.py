from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import json


# <:::: JSON ::::>

import json
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# JSON faylini o'qish
def load_buttons():
    with open("languages.json", "r", encoding="utf-8") as f:
        return json.load(f)

texts = load_buttons()

# Tugmalarni yaratish funktsiyasi
def create_menu_buttons(language):
    # Tugmalarni JSON faylidan olish
    button_texts = texts[language]["menu"]
    
    # Tugmalarni yaratish
    menu_buttons = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=button_texts["menu_button_1"]), KeyboardButton(text=button_texts["menu_button_2"])],
            [KeyboardButton(text=button_texts["menu_button_3"]), KeyboardButton(text=button_texts["menu_button_4"])]
        ],
        resize_keyboard=True,
    )
    return menu_buttons

# Tilga qarab tugmalarni yaratish
menu_button_uz = create_menu_buttons("uz")
menu_button_us = create_menu_buttons("us")
menu_button_ru = create_menu_buttons("ru")


# JSON faylini o'qish
# def load_buttons():
#     with open("buttons.json", "r", encoding="utf-8") as f:
#         return json.load(f)

# buttons = load_buttons()

# def create_menu_buttons(language):
#     # Tugmalarni JSON faylidan olish
#     button_texts = buttons[language]
    
#     # Tugmalarni yaratish
#     menu_buttons = ReplyKeyboardMarkup(
#         keyboard=[
#             [KeyboardButton(text=button_texts["menu_button_1"]), KeyboardButton(text=button_texts["menu_button_2"])],
#             [KeyboardButton(text=button_texts["menu_button_3"]), KeyboardButton(text=button_texts["menu_button_4"])]
#         ],
#         resize_keyboard=True,
#     )
#     return menu_buttons

# # Tilni tanlashga qarab tugma yaratish
# menu_button_uz = create_menu_buttons("uz")
# menu_button_us = create_menu_buttons("us")
# menu_button_ru = create_menu_buttons("ru")

# <:::: END JSON ::::>


# # Uzbek tilidagi tugmalar
# menu_button_uz = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="Biz haqimizda 👥"), KeyboardButton(text="Manzilimiz 📍")],
#         [KeyboardButton(text="Kurslar 📚"), KeyboardButton(text="Savol❓ va Takliflar 📝")]
#     ],
#     resize_keyboard=True,
# )

# # Ingliz tilidagi tugmalar
# menu_button_us = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="About Us 👥"), KeyboardButton(text="Our Address 📍")],
#         [KeyboardButton(text="Courses 📚"), KeyboardButton(text="Questions❓ and Suggestions 📝")]
#     ],
#     resize_keyboard=True,
# )

# # Rus tilidagi tugmalar
# menu_button_ru = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="О нас 👥"), KeyboardButton(text="Наш адрес 📍")],
#         [KeyboardButton(text="Курсы 📚"), KeyboardButton(text="Вопросы❓ и Предложения 📝")]
#     ],
#     resize_keyboard=True,
# )


# menus = {
#     "uz": ["Biz haqimizda 👥", "Manzilimiz 📍", "Kurslar 📚", "Savol❓ va Takliflar 📝"],
#     "us": ["About Us 👥", "Our Address 📍", "Courses 📚", "Questions❓ and Suggestions 📝"],
#     "ru": ["О нас 👥", "Наш адрес 📍", "Курсы 📚", "Вопросы❓ и Предложения 📝"],
# }

# menu_button = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder="Choose option...")

# # Tilga qarab tugmalarni qo'shamiz
# for language, options in menus.items():
#     for option in options:
#         menu_button.add(KeyboardButton(text=option))

# # Tugmalarni ikki ustunda ko'rsatish (max 2 ta tugma har qatorga)
# menu_button.adjust(2, repeat=True)

# computer_button = menu_button.as_markup(
#     resize_keyboard=True,
#     input_field_placeholder="Choose computer..."
# )


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

cours = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Python"), KeyboardButton(text="SMM")],
        [KeyboardButton(text="🔙Orqaga")]
    ],
    resize_keyboard=True,
)