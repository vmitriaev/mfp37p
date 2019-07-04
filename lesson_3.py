import telebot

bot = telebot.TeleBot("775565560:AAHM-IpOyDDoKeZtHU3CSJzLjSPsx7HEzOY")


@bot.message_handler(content_types=['text'])
def send_echo(message):
    #bot.reply_to(message, message.text)
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
