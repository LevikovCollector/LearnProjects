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
    #dp.add_handler(CommandHandler('planet', planet_info))
    #dp.add_handler(MessageHandler(Filters.text, check_constellation))
    dp.add_handler(CommandHandler('wordcount', count_words))
    dp.add_handler(CommandHandler('calc' , calculete, pass_args = True))

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

def check_constellation(bot, update):
    solar_system = ['mars','venus', 'mercury','jupiter','saturn','uranus','neptune','pluto']
    user_planet = str (update.message.text).lower()
    planet = None
    today = datetime.datetime.now().strftime('%Y/%m/%d')
    if user_planet in solar_system:
        if user_planet == 'mars':
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
            planet = ephem.Uranus (today)
        elif user_planet == 'neptune':
            planet = ephem.Neptune (today)
        elif user_planet == 'pluto':
            planet = ephem.Pluto(today)

        update.message.reply_text(ephem.constellation(planet)[1])
    else:
        update.message.reply_text('Введена неизвестная планета')


def count_words(bot, update):
    raw_text_from_user = str(update.message.text).lower()
    first_position = raw_text_from_user.find('"')
    last_position = raw_text_from_user.rfind('"')
    if first_position != last_position:
        text_from_user = raw_text_from_user [first_position:last_position+1]
        if(text_from_user != '' or text_from_user is not None):
            if text_from_user[0] == '"' and text_from_user[-1] == '"':
                words = text_from_user.split(' ')
                update.message.reply_text('Количеств слов: {0}'.format(str(len(words))))
            else:
              update.message.reply_text('Введите команду правильно /wordcount "<Ваш текст>"')
        else:
              update.message.reply_text('Введите команду правильно /wordcount "<Ваш текст>"')
    else:
        update.message.reply_text('Введите команду правильно /wordcount "<Ваш текст>"')

def calculete(bot,update, args):
    raw_user_message = ''.join(args).replace(' ','')
    if raw_user_message[-1] == '=':
        arithmetic_expression = raw_user_message.split('=')[0]
        arithmetic_result = None
        try:
            if(arithmetic_expression.find('+')!= -1):
                arithmetic_values = arithmetic_expression.split('+')
                arithmetic_result = execute_operation(arithmetic_values, '+')

            elif(arithmetic_expression.find('-')!= -1):
                arithmetic_values = arithmetic_expression.split('-')
                arithmetic_result = execute_operation(arithmetic_values , '-')
            elif(arithmetic_expression.find('/')!= -1):
                arithmetic_values = arithmetic_expression.split('/')
                arithmetic_result = execute_operation(arithmetic_values , '/')
            elif (arithmetic_expression.find('*') != -1):
                arithmetic_values = arithmetic_expression.split('*')
                arithmetic_result = execute_operation(arithmetic_values , '*')

            else:
                update.message.reply_text('Не известная команда ')

            if(arithmetic_result is not None):
                update.message.reply_text('Результат: {0}'. format(arithmetic_result))
        except ZeroDivisionError:
            update.message.reply_text('Деление на 0 запрещено! ')
    else:
        update.message.reply_text('Команда должна заканчиваться знаком равно ')

def check_value_type(value):
    if(value.find('.') == -1 and value.find(',') == -1):
        return int(value)
    else:
        return float(value.replace(',', '.'))

def execute_operation(values, operation):
    have_empty_values = False
    for value in values:
        if(value == ''):
            have_empty_values = True
            break
    if(not(have_empty_values)):
        if(operation == '+'):
            return check_value_type(values[0]) + check_value_type(values[1])
        elif (operation == '-'):
            return check_value_type(values[0]) - check_value_type(values[1])
        elif (operation == '/'):
            return check_value_type(values[0]) / check_value_type(values[1])
        elif (operation == '*'):
            return check_value_type(values[0]) * check_value_type(values[1])
    else:
        return "Есть пустые значения: {0}".format(values)

main()