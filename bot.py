from telebot import TeleBot
import time
from keyboard import generate_message_url, generate_contact

token = "6233567626:AAGLANCGh1c-RXkJ4fFr1yu40Is4KgUZVOQ"
bot = TeleBot(token)
channel_id = -1001680432171


@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    contact = bot.send_message(chat_id, "Meni MÔJIZAM bot emasligiga ishonch hosil qilishim uchun telefon raqamingizni qoldiring ☺️", reply_markup=generate_contact())
    bot.register_next_step_handler(contact, get_mail)


def get_mail(message):
    chat_id = message.chat.id
    get_contact = message.contact.phone_number
    bot.send_message(channel_id, "---------------------------------------------------------------------")
    bot.send_message(channel_id, f"Telefon nomer: {get_contact}")
    bot.send_photo(chat_id, open("photo_2023-05-16_07-44-05.jpg", "rb"))
    mail = bot.send_message(chat_id, 'Ma’lumotlarni doimiy bo’lishib borishim uchun - pochtangizni yuboring')
    bot.register_next_step_handler(mail, check_mail)
    return get_contact



def check_mail(message):
    chat_id = message.chat.id
    bot.send_message(channel_id, f"Po'chta: {message.text}")
    if message.text.isalnum():
        bot.send_message(chat_id, "Ma'lumot formati noto'gri! Po'chtangizni kiriting!")
        get_mail(message)
        return
    else:
        insta_story(message)


def insta_story(message):
    chat_id = message.chat.id
    insta = bot.send_photo(chat_id, open("photo_2023-05-16_07-44-23.jpg", "rb"), caption="• Barcha qatnashchilar jamlangan guruh ssilkasini qo’lga kiritish uchun, ushbu rasmni-Ôz storiesingizga joylab, meni sahifamni belgilang! (“Отметка” qiling) va bu stories 24 soat davomida saqlanib tursin.\n• Stories joylaganingiz haqidagi screenshotni yuboring va maxsus guruhga qo’shiling!")
    bot.register_next_step_handler(insta, check_story)


def check_story(message):
    from_chat_id = message.chat.id
    first_name = message.from_user.first_name
    user_name = message.from_user.username
    photo_file = message.photo[-1].file_id
    bot.send_photo(channel_id, photo_file, caption=f"Ism: {first_name}\n\nUsername: @{user_name}")
    if message.photo:
        bot.send_message(from_chat_id, "Ma'lumotlar tekshirish uchun yuborildi, tez orada sizga link yuboramiz!")
        time.sleep(5)
        go_canal(message)
    else:
        bot.send_message(from_chat_id, "Yo'riqnomaga amal qiling! Stories joylaganingiz haqidagi screenshotni  yuboring!")
        insta_story(message)
        return


def go_canal(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "To'lov skreenshotini quyidagi lichkaga yuboring, admin sizga guruhga qo'shilish uchun link yuboradi.\n\n👉 @the_dilnoza1", reply_markup=generate_message_url("https://t.me/the_dilnoza1"))


while True:
    try:
        print("Бот запущен !")
        bot.polling(none_stop=True)
    except Exception as exp:
        print(f'Произошла ошибка {exp.__class__.__name__}: {exp}')
        bot.stop_polling()
        time.sleep(5)
