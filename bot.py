import cfg
import telebot

bot = telebot.TeleBot(cfg.token)

@bot.message_handler(commands=['start'])
def mes_on_start(message):
    bot.send_message(message.from_user.id, 'Work it!)')
















if __name__ == '__main__':
    bot.polling(none_stop=True)
