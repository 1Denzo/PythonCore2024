#       Теперь нам нужно это интегрировать в бота. Логика будет такая:
# • После старта бот ждёт название города. Каждое сообщение, что пришлёт
#   пользователь, будет считаться таким названием.
# • Как только пользователь что-то присылает, бот подставляет город из
#   сообщения и отправляет запрос в службу погоды.
# • После ответа от службы бот формирует сообщение о погоде и отправляет
#   обратно пользователю.
# • Дальше всё повторяется: мы боту пишем город и получаем в ответ погоду
#   в этом город

import telebot
import requests
# подключаем модуль для Телеграма и библиотеку для работы с запросами

# Открываем файл для чтения
with open('Home_Made\\weather_bot\\tokens.txt', 'r') as file:
    # Читаем две строки из файла
    telegram_API_TOKEN = file.readline().strip()  # Первая строка
    openweathermap_token = file.readline().strip()  # Вторая строка

# указываем токен для доступа к боту
bot = telebot.TeleBot(telegram_API_TOKEN)
# приветственный текст
start_txt = 'Привет! \nНапиши мне название города, я скажу какая в нем сейчас погода.'
# обрабатываем старт бота
@bot.message_handler(commands=['start'])
def start(message):
# выводим приветственное сообщение
    bot.send_message(message.from_user.id, start_txt, parse_mode='Markdown')
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    city = message.text
    # формируем запрос
    url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+openweathermap_token
    # отправляем запрос на сервер и сразу получаем результат
    weather_data = requests.get(url).json()
    # получаем данные о температуре и о том, как она ощущается
    temperature = round(weather_data['main']['temp'])
    temperature_feels = round(weather_data['main']['feels_like'])
    # выводим значения на экран
    weather1 = 'Сейчас в городе '+city+" "+str(temperature)+' °C \n'+' Ощущается как '+str(temperature_feels)+' °C'
    print (weather1)
    bot.reply_to(message, weather1)
bot.infinity_polling()
