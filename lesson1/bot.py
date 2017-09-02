from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def main():
	API_KEY = '426807183:AAGHLEjcrwrvFKCPY_BAR8j7v45Sav61gMo'
	updater = Updater(API_KEY)

	dp = updater.dispatcher
	dp.add_handler(CommandHandler('start',greet_user)) # функция вызывается на команду start
	dp.add_handler(MessageHandler(Filters.text, echo_message))

	updater.start_polling()
	updater.idle()

def greet_user(bot, update): # bot, update - обязательные параметры при работе с ботом
	text_for_user = 'Привет новый пользователь!'
	print(text_for_user)
	update.message.reply_text(text_for_user)

def echo_message(bot, update):
	user_text = update.message.text
	print(user_text)
	update.message.reply_text(user_text)


main()