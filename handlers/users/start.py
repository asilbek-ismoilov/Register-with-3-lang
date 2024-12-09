# from aiogram.types import Message, CallbackQuery
# from loader import dp, db
# from aiogram.filters import CommandStart
# from keyboard_buttons.default.menu import menu_button_uz, menu_button_us, menu_button_ru
# from keyboard_buttons.inline.inline_val import language
# from aiogram.fsm.context import FSMContext
# from languages import texts  # Import the texts from languages.py

# @dp.message(CommandStart())
# async def start_command(message: Message):
#     await message.answer(
#         text=texts["uz"]["start_message"],  # Use the start message for Uzbek
#         parse_mode="html",
#         reply_markup=language
#     )   

# @dp.callback_query(lambda c: c.data in ["uz", "us", "ru"])
# async def edit(callback: CallbackQuery, state: FSMContext):
#     await state.clear()
#     await callback.message.delete()

#     selected_language = callback.data
#     full_name = callback.from_user.full_name
#     telegram_id = callback.from_user.id

#     # Foydalanuvchini bazadan tekshirish
#     user = db.select_user_by_id(telegram_id=telegram_id)

#     # Foydalanuvchining tilini yangilash yoki qo'shish
#     if user is None:
#         db.add_user(full_name=full_name, telegram_id=telegram_id, language=selected_language)
#     else:
#         db.update_user_language(telegram_id=telegram_id, language=selected_language)

#     await callback.message.answer(texts[selected_language]["selected_language"])

#     menu_buttons = {
#         "uz": menu_button_uz,
#         "us": menu_button_us,
#         "ru": menu_button_ru
#     }

#     # Send the welcome message from languages.py
#     await callback.message.answer(
#         text=texts[selected_language]["welcome_message"].format(full_name=full_name),
#         parse_mode='html',
#         reply_markup=menu_buttons[selected_language]
#     )



# JSON
import json
from aiogram.types import Message, CallbackQuery
from loader import dp, db
from aiogram.filters import CommandStart
# from keyboard_buttons.default.menu import menu_button_uz, menu_button_us, menu_button_ru
from keyboard_buttons.default.menu import create_menu_buttons
from keyboard_buttons.inline.inline_val import language
from aiogram.fsm.context import FSMContext

# JSON faylini o'qish
def load_texts():
    with open("languages.json", "r", encoding="utf-8") as f:
        return json.load(f)

texts = load_texts()

@dp.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        text=texts["uz"]["start_message"],  # Use the start message for Uzbek
        parse_mode="html",
        reply_markup=language
    )

@dp.callback_query(lambda c: c.data in ["uz", "us", "ru"])
async def edit(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.delete()

    selected_language = callback.data
    full_name = callback.from_user.full_name
    telegram_id = callback.from_user.id

    # Foydalanuvchini bazadan tekshirish
    user = db.select_user_by_id(telegram_id=telegram_id)

    # Foydalanuvchining tilini yangilash yoki qo'shish
    if user is None:
        db.add_user(full_name=full_name, telegram_id=telegram_id, language=selected_language)
    else:
        db.update_user_language(telegram_id=telegram_id, language=selected_language)

    await callback.message.answer(texts[selected_language]["selected_language"])

    # Send the welcome message from JSON file
    await callback.message.answer(
        text=texts[selected_language]["welcome_message"].format(full_name=full_name),
        parse_mode='html',
        reply_markup=create_menu_buttons(selected_language)
    )
