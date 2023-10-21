from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_cansel = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

btn_cansel = KeyboardButton(text='Отмена')

kb_cansel.add(btn_cansel)
