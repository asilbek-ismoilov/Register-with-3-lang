from aiogram.types import Message
from loader import dp, db
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
import json

def load_texts():
    with open("languages.json", "r", encoding="utf-8") as f:
        return json.load(f)

texts = load_texts()

@dp.message(Command("about"))
async def about_commands(message: Message, state: FSMContext):
    user = db.select_user_by_id(message.from_user.id)

    language = "uz" 
    if user:
        language = user[5] 

    text = texts.get(language, {}).get("about", "Tilga mos matn topilmadi.")

    await message.answer(text, parse_mode='html')
    await state.clear()