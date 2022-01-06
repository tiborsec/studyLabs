import telebot

CHAVE_API = "5021747761:AAGYbQ7C8CJL5DFWeJOa5PWHVVrkSPjFaV8"

bot = telebot.TeleBot(CHAVE_API)

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    bot.reply_to(mensagem, "Olá, Aqui é o 7ib0r")

bot.polling()