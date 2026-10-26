import telebot
from telebot import types
import random
import datetime

BOT_TOKEN = "8953790961:AAGrA7UjVv9JdVAGIDjhcU9D0mcyCi7dURM"
bot = telebot.TeleBot(BOT_TOKEN)

# Словарь: знак зодиака -> эмодзи
zodiacs = {
    "♈ Овен": "♈", "♉ Телец": "♉", "♊ Близнецы": "♊",
    "♋ Рак": "♋", "♌ Лев": "♌", "♍ Дева": "♍",
    "♎ Весы": "♎", "♏ Скорпион": "♏", "♐ Стрелец": "♐",
    "♑ Козерог": "♑", "♒ Водолей": "♒", "♓ Рыбы": "♓"
}

spheres = ["в работе", "в личной жизни", "в финансах", "в здоровье", "в обучении", "в общении с близкими"]
moods = ["удачный", "спокойный", "напряженный", "непредсказуемый", "продуктивный", "вдохновляющий"]
advices = [
    "не бойся принимать решения", "удели время отдыху", "прислушайся к интуиции",
    "сделай первый шаг", "не торопи события", "будь внимателен к деталям",
    "позволь себе что-то новое", "доверься близким"
]

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    buttons = [types.KeyboardButton(sign) for sign in zodiacs.keys()]
    markup.add(*buttons)
    
    bot.reply_to(message, "Привет! Я твой личный астролог. Выбери свой знак зодиака на клавиатуре ниже, чтобы получить предсказание на сегодня. 🔮", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in zodiacs)
def send_horoscope(message):
    sign = message.text
    today = datetime.date.today().strftime("%d.%m.%Y")
    
    sphere = random.choice(spheres)
    mood = random.choice(moods)
    advice = random.choice(advices)
    
    response = (
        f"🔮 **Гороскоп для {sign} на {today}:**\n\n"
        f"День будет **{mood}** {sphere}.\n"
        f"Совет дня: {advice}.\n\n"
        f"✨ Хорошего дня!"
    )
    
    bot.reply_to(message, response, parse_mode='Markdown')

@bot.message_handler(func=lambda message: True)
def unknown(message):
    bot.reply_to(message, "Пожалуйста, выбери знак зодиака из списка ниже 👇")

print("🔮 Бот-гороскоп запущен...")
bot.polling(none_stop=True)