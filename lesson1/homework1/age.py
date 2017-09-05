

user_age = int (input('Введите свой возраст: '))

if user_age >= 0 and user_age <=2:
	print ('Вам еще нужно вырасти')

if user_age >= 3 and user_age <=6:
	print ('Вы ходите в детский сад')

elif user_age >= 7 and user_age <= 18:
	print ('Вы ходите в школу')

elif user_age >= 19 and user_age <= 23:
	print ('Вы ходите в институт')

elif user_age >= 24:
	print ('Вы ходите на работу')