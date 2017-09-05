from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem
import datetime

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def main():
	API_KEY = '426807183:AAGHLEjcrwrvFKCPY_BAR8j7v45Sav61gMo'
	updater = Updater(API_KEY)

	dp = updater.dispatcher
	dp.add_handler(CommandHandler('start',greet_user)) # функция вызывается на команду start
	#dp.add_handler(MessageHandler(Filters.text, echo_message))
	dp.add_handler(CommandHandler('planet', planet_info))


	updater.start_polling()
	updater.idle()

def greet_user(bot, update): # bot, update - обязательные параметры при работе с ботом
	text_for_user = 'Привет новый пользователь!'
	print(text_for_user)
	update.message.reply_text(update)
	
def echo_message(bot, update):
	user_text = update.message.text
	print(user_text)
	update.message.reply_text(user_text)

def planet_info(bot, update):
	update.message.reply_text('Введите название планеты на английском: ')
	user_planet = str(update.message.text).lower()
	planet = None
	today = datetime.datetime.now().strftime('%Y/%m/%d')
	if  user_planet == 'mars':
		planet = ephem.Mars(today)
	elif user_planet == 'venus':
		planet = ephem.Venus(today)
	elif user_planet == 'mercury':
		planet = ephem.Mercury(today)
	elif user_planet == 'jupiter':
		planet = ephem.Jupiter(today)
	elif user_planet == 'saturn':
		planet = ephem.Saturn(today)			
	elif user_planet == 'uranus':
		planet = ephem.Uranus(today)	
	elif user_planet == 'neptune':
		planet = ephem.Neptune(today)	
	elif user_planet == 'pluto':
		planet = ephem.Pluto(today)	

	update.message.reply_text(str(ephem.constellation(planet)[1]))

main()