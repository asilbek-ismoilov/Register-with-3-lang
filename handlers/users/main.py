from loader import dp, bot, ADMINS, db
from aiogram import F
from keyboard_buttons.default.menu import menu_button, course_buttons, create_menu_buttons, back_button
from aiogram.types import Message,CallbackQuery, ContentType
from aiogram.fsm.context import FSMContext
from keyboard_buttons.default.menu import menu_button
from states.help_stt import AdminStates, AdminStates, create_inline_keyboard
from aiogram import types
import logging
from aiogram.fsm.context import FSMContext
import json

def load_texts():
    with open("languages.json", "r", encoding="utf-8") as f:
        return json.load(f)

texts = load_texts()

def is_about_us_message(message_text):
    possible_texts = [
        texts.get(lang, {}).get("menu", {}).get("menu_button_1", "")
        for lang in texts
    ]
    return message_text in possible_texts

@dp.message(lambda message: is_about_us_message(message.text))
async def about_us(message: Message, state: FSMContext):
    user = db.select_user_by_id(message.from_user.id)

    language = "uz" 
    if user:
        language = user[5] 

    text = texts.get(language, {}).get("about_us", "Tilga mos matn topilmadi.")

    await message.answer(text, parse_mode='html')
    await state.clear()



def is_location_message(message_text):
    possible_texts = [
        texts.get(lang, {}).get("menu", {}).get("menu_button_2", "")
        for lang in texts
    ]
    return message_text in possible_texts


@dp.message(lambda message: is_location_message(message.text))
async def location(message: Message, state: FSMContext):
    user = db.select_user_by_id(message.from_user.id)
    language = "uz"

    if user:
        language = user[5]

    text = texts.get(language, {}).get("location", "Matn topilmadi.")

    await message.answer_location(latitude=40.102545165025, longitude=65.3734143754646)
    await message.answer(text, parse_mode='html')
    await state.clear()


@dp.message(lambda message: message.text in ["Kurslar 📚", "Courses 📚", "Курсы 📚"])
async def cours_info(message: Message, state: FSMContext): 
    user = db.select_user_by_id(message.from_user.id)
    language = "uz"

    if user:
        language = user[5]
    
    if language == "uz":
        await message.answer("Menu dan birini tanlang", reply_markup=course_buttons(language))
    elif language == "ru":
        await message.answer("Выберите одну из меню", reply_markup=course_buttons(language))
    elif language == "us":
        await message.answer("Choose one of the menu", reply_markup=course_buttons(language))
    
    await state.clear()

# ------------------------------------------------------------------

@dp.message(lambda message: message.text in ["Orqaga🔙", "Back🔙", "Назад🔙"])
async def exit(message: Message):
    user = db.select_user_by_id(message.from_user.id)
    language = "uz"

    if user:
        language = user[5]
    
    if language == "uz":
        await message.answer("Menyu", reply_markup=create_menu_buttons(language))
    elif language == "ru":
        await message.answer("Меню", reply_markup=create_menu_buttons(language))
    elif language == "us":
        await message.answer("Menu", reply_markup=create_menu_buttons(language))

def admin_send_message(message_text):
    possible_texts = [
        texts.get(lang, {}).get("menu", {}).get("menu_button_4", "")
        for lang in texts
    ]
    return message_text in possible_texts

@dp.message(lambda message: admin_send_message(message.text))
async def admin_message(message: Message, state: FSMContext):

    user = db.select_user_by_id(message.from_user.id)
    language = "uz"

    if user:
        language = user[5]
        
    if language == "uz":
        text = "Admin uchun xabar yuboring:"
    elif language == "ru":
        text = "Отправьте сообщение админу:"
    elif language == "us":
        text = "Send a message to the admin:"

    await message.answer(text,reply_markup=back_button(language))
    await state.set_state(AdminStates.waiting_for_admin_message)

@dp.message(AdminStates.waiting_for_admin_message, F.content_type.in_([
    ContentType.TEXT, ContentType.AUDIO, ContentType.VOICE, ContentType.VIDEO,
    ContentType.PHOTO, ContentType.ANIMATION, ContentType.STICKER, 
    ContentType.LOCATION, ContentType.DOCUMENT, ContentType.CONTACT,
    ContentType.VIDEO_NOTE
]))

async def handle_admin_message(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name or ""  # Some users may not have a last name
    telegram_id = message.from_user.id
    user = db.select_user(telegram_id=telegram_id)
    language = "uz"

    if user:
        language = user[5]

    if user[4] == "998999999999":
        if username:
            user_identifier = f"@{username}"
        else:
            user_identifier = f"{first_name} {last_name}".strip() 
    else: 
        if language == "uz":
            text = "Telefon"
        elif language == "ru":
            text = "Телефон"
        elif language == "us":
            text = "Phone"

        user_identifier = f"{user[2]} {user[3]}\n{text}: {user[4]}"

    user_text = texts.get(language, {}).get("text_admin", "Matn topilmadi.")
    user_mes = texts.get(language, {}).get("text_m", "Matn topilmadi.")

    video_note = message.video_note
    inline_keyboard = create_inline_keyboard(user_id)
    for admin_id in ADMINS:
        try:
            if video_note:
                await bot.send_video_note(
                    admin_id,
                    video_note.file_id,
                    reply_markup=inline_keyboard
                )
            elif message.text:
                await bot.send_message(
                    admin_id,
                    f"{user_text} {user_identifier}\n{user_mes}:\n{message.text}",
                    reply_markup=inline_keyboard
                )
            elif message.audio:
                await bot.send_audio(
                    admin_id,
                    message.audio.file_id,
                    caption=f"{user_text} {user_identifier}\nAudio {user_mes}",
                    reply_markup=inline_keyboard
                )
            elif message.voice:
                await bot.send_voice(
                    admin_id,
                    message.voice.file_id,
                    caption=f"{user_text} {user_identifier}\nVoice {user_mes}",
                    reply_markup=inline_keyboard
                )
            elif message.video:
                await bot.send_video(
                    admin_id,
                    message.video.file_id,
                    caption=f"{user_text} {user_identifier}\nVideo {user_mes}",
                    reply_markup=inline_keyboard
                )
            elif message.photo:
                await bot.send_photo(
                    admin_id,
                    message.photo[-1].file_id,  
                    caption=f"{user_text} {user_identifier}\nPhoto {user_mes}",
                    reply_markup=inline_keyboard
                )
            elif message.animation:
                await bot.send_animation(
                    admin_id,
                    message.animation.file_id,
                    caption=f"{user_text} {user_identifier}\nGIF {user_mes}",
                    reply_markup=inline_keyboard
                )
            elif message.sticker:
                await bot.send_sticker(
                    admin_id,
                    message.sticker.file_id,
                    reply_markup=inline_keyboard
                )
            elif message.location:
                await bot.send_location(
                    admin_id,
                    latitude=message.location.latitude,
                    longitude=message.location.longitude,
                    reply_markup=inline_keyboard
                )
            elif message.document:
                await bot.send_document(
                    admin_id,
                    message.document.file_id,
                    caption=f"{user_text} {user_identifier}\nDocument {user_mes}",

                    reply_markup=inline_keyboard
                )
            elif message.contact:
                await bot.send_contact(
                    admin_id,
                    phone_number=message.contact.phone_number,
                    first_name=message.contact.first_name,
                    last_name=message.contact.last_name or "",
                    reply_markup=inline_keyboard
                )
        except Exception as e:
            logging.error(f"Error sending message to admin {admin_id}: {e}")

    await state.clear()
    await bot.send_message(user_id, "Admin sizga javob berishi mumkin.",reply_markup=menu_button)

# Callback query handler for the reply button
@dp.callback_query(lambda c: c.data.startswith('reply:'))
async def process_reply_callback(callback_query: CallbackQuery, state: FSMContext):
    user_id = int(callback_query.data.split(":")[1])
    print(user_id)
    telegram_id = callback_query.from_user.id
    print(telegram_id)
    await callback_query.message.answer("Javobingizni yozing. Sizning javobingiz foydalanuvchiga yuboriladi.")
    await state.update_data(reply_user_id=user_id)
    await state.set_state(AdminStates.waiting_for_reply_message)
    await callback_query.answer()

# Handle admin reply and send it back to the user
@dp.message(AdminStates.waiting_for_reply_message)
async def handle_admin_reply(message: Message, state: FSMContext):
    data = await state.get_data()
    original_user_id = data.get('reply_user_id')

    if original_user_id:
        try:
            if message.text:
                await bot.send_message(original_user_id, f"Admin javobi:\n{message.text}", reply_markup=menu_button)
            
            elif message.voice:
                await bot.send_voice(original_user_id, message.voice.file_id, reply_markup=menu_button)

            elif message.video_note:
                await bot.send_video_note(original_user_id, message.video_note.file_id, reply_markup=menu_button)

            elif message.audio:
                await bot.send_audio(original_user_id, message.audio.file_id, reply_markup=menu_button)
            
            elif message.sticker:
                await bot.send_sticker(original_user_id, message.sticker.file_id, reply_markup=menu_button)
            
            elif message.video:
                await bot.send_video(original_user_id, message.video.file_id, reply_markup=menu_button)

            await state.clear()  # Clear state after sending the reply
        except Exception as e:
            logging.error(f"Error sending reply to user {original_user_id}: {e}")
            await message.reply("Xatolik: Javob yuborishda xato yuz berdi.")
    else:
        await message.reply("Xatolik: Javob yuborish uchun foydalanuvchi ID topilmadi.")
