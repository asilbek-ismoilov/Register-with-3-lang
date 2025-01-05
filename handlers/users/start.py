
import json
from aiogram.types import Message, CallbackQuery
from loader import dp, db
from aiogram.filters import CommandStart
from keyboard_buttons.default.menu import create_menu_buttons
from keyboard_buttons.inline.inline_val import language
from aiogram.fsm.context import FSMContext

def load_texts():
    with open("languages.json", "r", encoding="utf-8") as f:
        return json.load(f)

texts = load_texts()

@dp.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        text="Tilni tanlang 🇺🇿 | Choose a language 🇺🇸 | Выберите язык 🇷🇺", 
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

    user = db.select_user_by_id(telegram_id=telegram_id)

    await callback.message.answer(
        text=texts[selected_language]["selected_language"],
        reply_markup=create_menu_buttons(selected_language)
    )

    if user is None:
        db.add_user(full_name=full_name, telegram_id=telegram_id, language=selected_language)
        await callback.message.answer(
            text=texts[selected_language]["welcome_message"].format(full_name=full_name),
            parse_mode='html'
        )
    else:
        db.update_user_language(telegram_id=telegram_id, language=selected_language)
        # await callback.message.answer(
        #     text=f"Assalomu alaykum! {full_name}",
        #     parse_mode='html'
        # )
    
def language_message(message_text):
    possible_texts = [
        texts.get(lang, {}).get("menu", {}).get("menu_button_5", "")
        for lang in texts
    ]
    return message_text in possible_texts

@dp.message(lambda message: language_message(message.text))
async def language_us(message: Message, state: FSMContext):

    await message.answer("Tilni tanlang 🇺🇿 | Choose a language 🇺🇸 | Выберите язык 🇷🇺", parse_mode='html', reply_markup=language) 
    await state.clear()
