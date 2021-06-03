from telebot import types, TeleBot

bot = TeleBot('1823110206:AAFUhMdeOtog64fCGENHNEwJs_B0Z2alUss')

topics = ["Урок 1. Переменные, print, input", "Урок 2. Типы данных, арифметические операции,"]
lessons = {}

for topic in topics:
    lessons[topic] = ''



lesson = 0

@bot.message_handler(content_types=['text', 'document', 'audio'])

def get_text_messages(message):
    msg = message.text
    if msg == "привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif msg == "/help":
        bot.send_message(message.from_user.id, "Напиши 'привет' или узнай, что я могу, написав 'что ты можешь?'")
    elif msg == "что ты можешь?" or msg == "что ты можешь":
        bot.send_message(message.from_user.id, "Я могу напомнить тебе тему конспектом")
    elif msg == "конспект урока":
        bot.send_message('Вот темы всех уроков:', topics)
        bot.send_message('Напиши номер урока')
        bot.register_next_step_handler(message, lesson_num)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

def lesson_num(message):
    global lesson
    global topics
    while lesson == 0:
        try:
            lesson = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no= types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    question = 'Тебе нужен ', topics[lesson - 1], '?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)

def callback_worker(call, message):
    if call.data == "yes":
        bot.send_message(message.from_user.id, lessons[topic[lesson - 1]])
    elif call.data == "no":
        bot.send_message('Напиши номер урока')

bot.polling(none_stop=True, interval=0)
