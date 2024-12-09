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

reg_courses = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text= "📋 Kursga yozilish", callback_data="reg_cours")]
    ]
)

confirmation = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text= "Bekor qilish ❌", callback_data="cancel"), InlineKeyboardButton(text= "O'zgartirish 📝", callback_data="change"), InlineKeyboardButton(text= "Tasdiqlash ✅", callback_data="right")]
    ]
)
