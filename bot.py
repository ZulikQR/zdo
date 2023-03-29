import telebot
import types


bot = telebot.TeleBot("6141144750:AAFXMLBbYqAXu0BZzJbH-dkFJlJqoDg9coI")
admin_id = "5872755751"

parse_mode = 'html'

@bot.message_handler(commands=['start'])
def start_handler(message):
    markup = telebot.types.InlineKeyboardMarkup(row_width=2)
    itembtn1 = telebot.types.InlineKeyboardButton('Жалоба', callback_data='complaint')
    itembtn2 = telebot.types.InlineKeyboardButton('Вопрос', callback_data='question')
    itembtn3 = telebot.types.InlineKeyboardButton('Правила', callback_data='rules')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id, '<code>Добро пожаловать в</code> <b>ZDO!</b>', reply_markup=markup , parse_mode = "html")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'complaint':
        bot.send_message(call.message.chat.id, '<b>Напишите свою жалобу</b>' , parse_mode = "html")
        bot.register_next_step_handler(call.message, save_complaint)
    elif call.data == 'question':
        bot.send_message(call.message.chat.id, '<b>Какой у вас вопрос?</b>' , parse_mode = "html")
        bot.register_next_step_handler(call.message, save_question)
    elif call.data == 'rules':
        bot.send_message(call.message.chat.id, """ 

🗓 <b>Правила чата:</b>
🔺

🔸 Мат допустим, и без оскорблений в чужой адрес

🔹 Реклама групп и каналов в любом виде, продажа наркотиков, оружия, детского порно
🥾 [Бан] [Рекламу обговаривать с @zulikwb]
👤 - Подпишитесь на мой канал/группу (пример)

🔹 Шок - контент и порно
🙊 [Бан]
👤 - Гифки и стикеры с порно или с кровью

🔹 Оскорбление
🙊 [Варн]
👤 - Иди нахуй тварь (пример)

🔹 Срач в чате после предупреждения Администрации
🙊 [Мут - 1 час + Варн]
👤 - Продолжение срача

🔹Оскорбление родни 
🙊 [Бан]
👤 - Я твою маму ебал (пример)

🔹Попытка вреду группе
🙊 [Бан без возможности возврата]
👤 - Спам атаки и т.д

🔹Политика
🙊 [Варн + Мут , пов. = Бан]
👤- Зеленский пидорас (пример)

🔹Срач в войсчате 
🙊 [Мут , пов. = запрет на войсчаты]
👤 - Не срись в войс чате

🔹Предложка работы / вакансий 
🙊 [Мут , варн]
👤- Есть работка (пример)

❗️Если вы заметили нарушение правил которых не заметили админы просим ответить на сообщение коммандой @admin

🗽 Администрация оставляет за собой право на изменение правил""" , parse_mode = 'html')

def save_complaint(message):
    chat_id = message.chat.id
    username = message.from_user.username
    complaint = message.text
    bot.send_message(admin_id, f"<b>Жалоба:</b>\nОт - @{username}\n\nЖалоба - {complaint}")
    bot.send_message(chat_id, "<code>Ваша жалоба была успешно отправлена админу</code>" , parse_mode = 'html')

def save_question(message):
    chat_id = message.chat.id
    username = message.from_user.username
    question = message.text
    bot.send_message(admin_id, f"Вопрос\nОт - @{username}\n\nВопрос - {question}",
                     reply_markup=telebot.types.InlineKeyboardMarkup()
                     .add(telebot.types.InlineKeyboardButton('Ответить', callback_data='answer')))
    bot.send_message(chat_id, "<code>Ваш вопрос был успешно отправлен админу</code>" , parse_mode = 'html')

bot.polling()
