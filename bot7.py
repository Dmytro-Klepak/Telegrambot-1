import telebot

token = '7866250534:AAGsX4prZEQbQpNRCTMPmYyTF411yYkJt28'
# Замініть 'YOUR_TOKEN' на ваш реальний токен
bot = telebot.TeleBot('7866250534:AAGsX4prZEQbQpNRCTMPmYyTF411yYkJt28')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()

if name == 'main':  # Перевіряє, чи файл запущений напряму 
    bot.polling(none_stop=True)  # Запускає постійне опитування сервера Telegram для отримання нових повідомлень