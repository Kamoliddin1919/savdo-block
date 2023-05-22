from telebot import types


def generate_contact():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    reg_button = types.KeyboardButton(text="📤Kontakt yuborish", request_contact=True)
    keyboard.row(reg_button)
    return keyboard


def generate_message_url(url):
    keyboard = types.InlineKeyboardMarkup()
    btn_url = types.InlineKeyboardButton(text="Adminga yozish!", url=url)
    keyboard.row(btn_url)
    return keyboard
