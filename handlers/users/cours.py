from loader import dp, db, bot, ADMINS
from aiogram import F
import re
from states.register_stt import SingUp
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboard_buttons.default.menu import tel_buttons, create_menu_buttons, course_buttons
from aiogram.types import CallbackQuery
from keyboard_buttons.inline.inline_val import create_inline_buttons, confirmation_buttons
import json

def load_texts():
    with open("languages.json", "r", encoding="utf-8") as f:
        return json.load(f)

texts = load_texts()

# <-------------------------- Python qismi start ----------------------------------------------------------------------------->

@dp.message(F.text == "Python")
async def show_python_course_details(message: Message,state:FSMContext):
    await state.clear()
    await state.update_data(cours = "Python")
    
    user = db.select_user_by_id(message.from_user.id)

    language = "uz" 
    if user:
        language = user[5] 

    python_course_info = texts.get(language, {}).get("python", "Tilga mos matn topilmadi.")

    await message.answer(python_course_info, parse_mode="Markdown",reply_markup=create_inline_buttons(language))

# <-------------------------- Python qismi finish ----------------------------------------------------------------------------->

# <-------------------------- SMM qismi start ----------------------------------------------------------------------------->

@dp.message(F.text == "SMM")
async def show_python_course_details(message: Message,state:FSMContext):
    await state.clear()
    await state.update_data(cours = "SMM")

    user = db.select_user_by_id(message.from_user.id)

    language = "uz" 
    if user:
        language = user[5] 

    python_course_info = texts.get(language, {}).get("smm", "Tilga mos matn topilmadi.")

    await message.answer(python_course_info, parse_mode="Markdown", reply_markup=create_inline_buttons(language))


# <-------------------------- SMM qismi finish ----------------------------------------------------------------------------->

    
@dp.callback_query(F.data == "reg_cours")
async def reg_cours(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    telegram_id = callback.from_user.id
    user = db.select_user(telegram_id=telegram_id)

    data = await state.get_data()
    cours = data.get("cours")

    language = "uz" 
    if user:
        language = user[5] 


    if user:
        if user[4] == "998999999999":
            await callback.message.answer(texts.get(language, {}).get("name", "Tilga mos matn topilmadi."), parse_mode='html', reply_markup=None)
            await state.set_state(SingUp.name)
        else:
            if language == "uz":
                f_text = f"<blockquote>Ma'lumotlaringiz to'g'rimi tekshiring ❗️❗️❗️</blockquote>\nKurs: {cours} \n<b>Ism-Familiya</b>: {user[2]} {user[3]} \n<b>Tel</b>: {user[4]}"
            elif language == "ru":
                f_text = f"<blockquote>Проверьте правильность ваших данных ❗️❗️❗️</blockquote>\nКурс: {cours} \n<b>Фамилия и имя</b>: {user[2]} {user[3]} \n<b>Телефон</b>: {user[4]}"
            elif language == "us": 
                f_text = f"<blockquote>Check if your information is correct ❗️❗️❗️</blockquote>\nCourse: {cours} \n<b>Full Name</b>: {user[2]} {user[3]} \n<b>Phone</b>: {user[4]}"
            
            await callback.message.answer(f_text, reply_markup=confirmation_buttons(language), parse_mode='html')

# name
@dp.message(F.text, SingUp.name)
async def send_advert(message:Message,state:FSMContext):
    name = message.text

    user = db.select_user_by_id(message.from_user.id)

    language = "uz" 
    if user:
        language = user[5] 

    if name.isalpha():
        await state.update_data(name = name)
        await message.answer(texts.get(language, {}).get("surname", "Tilga mos matn topilmadi."), parse_mode='html')
        await state.set_state(SingUp.surname)
    else:
        await message.delete()
        await message.answer(texts.get(language, {}).get("check_name", "Tilga mos matn topilmadi."), parse_mode='html')
        

@dp.message(SingUp.name)
async def name_del(message:Message, state:FSMContext):
    await message.delete()

    user = db.select_user_by_id(message.from_user.id)

    language = "uz" 
    if user:
        language = user[5] 

    await message.answer(texts.get(language, {}).get("check_name", "Tilga mos matn topilmadi."), parse_mode='html')


# surname
@dp.message(F.text, SingUp.surname)
async def surname(message:Message, state:FSMContext):
    surname = message.text

    user = db.select_user_by_id(message.from_user.id)

    language = "uz" 
    if user:
        language = user[5] 

    if surname.isalpha():
        await state.update_data(surname = surname)
        await message.answer(texts.get(language, {}).get("phone", "Tilga mos matn topilmadi."), reply_markup=tel_buttons(language), parse_mode='html')
        await state.set_state(SingUp.tel)
    else:
        await message.delete()
        await message.answer(texts.get(language, {}).get("check_surname", "Tilga mos matn topilmadi."),  parse_mode='html')


@dp.message(SingUp.surname)
async def surname_del(message:Message, state:FSMContext):
    await message.delete()

    user = db.select_user_by_id(message.from_user.id)

    language = "uz" 
    if user:
        language = user[5] 

    await message.answer(texts.get(language, {}).get("check_surname", "Tilga mos matn topilmadi."), parse_mode='html')

@dp.message(F.contact | F.text, SingUp.tel)
async def phone_number(message: Message, state: FSMContext):

    user = db.select_user_by_id(message.from_user.id)

    language = "uz" 
    if user:
        language = user[5]

    if message.contact:
        phone = message.contact.phone_number
    else:
        phone = message.text

    data = await state.get_data()

    name = data.get("name")
    surname = data.get("surname")
    cours = data.get("cours")

    uzbek_phone_pattern = r"^(\+998|998)[0-9]{9}$"
    if re.match(uzbek_phone_pattern, phone):
        await state.update_data(phone=phone)
        if language == "uz":
            f_text = f"<blockquote>Ma'lumotlaringiz to'g'rimi tekshiring ❗️❗️❗️</blockquote>\nKurs: {cours} \n<b>Ism-Familiya</b>: {name} {surname} \n<b>Tel</b>: {phone}"
        elif language == "ru":
            f_text = f"<blockquote>Проверьте, верны ли ваши данные ❗️❗️❗️</blockquote>\nКурс: {cours} \n<b>Имя-Фамилия</b>: {name} {surname} \n<b>Тел</b>: {phone}"
        elif language == "us": 
            f_text = f"<blockquote>Check if your information is correct ❗️❗️❗️</blockquote>\nCourse: {cours} \n<b>Name-Surname</b>: {name} {surname} \n<b>Phone</b>: {phone}"

        
        await message.answer(f_text, reply_markup=confirmation_buttons(language) , parse_mode='html') 
    else:
        await message.delete()
        await message.answer(texts.get(language, {}).get("check_phone", "Tilga mos matn topilmadi."), parse_mode='html')



@dp.message(SingUp.tel)
async def phone_number_del(message:Message):
    await message.delete()

    user = db.select_user_by_id(message.from_user.id)

    language = "uz" 
    if user:
        language = user[5] 

    await message.answer(texts.get(language, {}).get("check_phone", "Tilga mos matn topilmadi."), parse_mode='html')
    await message.delete()


@dp.callback_query(F.data == "cancel")
async def cancel(callback:CallbackQuery,state:FSMContext):
    await state.clear()
    await callback.message.delete()

    print(callback.from_user.id)
    user = db.select_user_by_id(callback.from_user.id)
    print(user)

    language = "uz" 

    if user:
        language = user[5] 

    print(language)

    if language == "uz":
        text = "<b>Menyu</b>"
    elif language == "ru":
        text = "<b>Меню</b>"
    elif language == "us":
        text = "<b>Menu</b>"

    await callback.message.answer(text, parse_mode='html', reply_markup=create_menu_buttons(language))

@dp.callback_query(F.data == "change")
async def edit(callback:CallbackQuery,state:FSMContext):
    await state.clear()
    await callback.message.delete()

    telegram_id = callback.from_user.id
    user = db.select_user_by_id(telegram_id=telegram_id)

    language = "uz" 
    if user:
        language = user[5] 

    await callback.message.answer(texts.get(language, {}).get("again", "Tilga mos matn topilmadi."), parse_mode='html', reply_markup=course_buttons(language))
    await state.set_state(SingUp.name)


@dp.callback_query(F.data == "right")
async def right(callback:CallbackQuery, state:FSMContext):
    telegram_id = callback.from_user.id
    user = db.select_user(telegram_id=telegram_id)

    language = "uz" 
    if user:
        language = user[5] 

    await callback.message.answer(texts.get(language, {}).get("register_text", "Tilga mos matn topilmadi."), reply_markup=create_menu_buttons(language) , parse_mode='html')
    await callback.message.delete()

    data = await state.get_data()
    cours = data.get("cours")

    if user:
        if user[4] == "998999999999":
            name = data.get("name")
            surname = data.get("surname")
            phone = data.get("phone")

            text = f"Yangi o'quvchi 👤\n<blockquote>Kurs: {cours} \n<b>Ism-Familiya</b>: {name} {surname} \n<b>Tel</b>: {phone}</blockquote>"
            for admin in ADMINS:
                await bot.send_message(admin, text, parse_mode='html')

            full_name = f"{name} {surname}"
            db.add_user(telegram_id=callback.from_user.id, full_name=full_name, name=name, surname=surname, phone=phone)
        else:
            text = f"Yangi o'quvchi 👤\n<blockquote>Kurs: {cours} \n<b>Ism-Familiya</b>: {user[2]} {user[3]} \n<b>Tel</b>: {user[4]}</blockquote>"
            for admin in ADMINS:
                await bot.send_message(admin, text, parse_mode='html')

    await state.clear()
