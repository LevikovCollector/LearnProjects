print ('Погода за 3 дня')
print ('-'*1000)

date = None
temperature = None
meteo = []

for day in range (0, 3):
	date = input('Введите дату (день {0}): '.format(day+1))
	temperature = input('Введите температуру: ')
	meteo.append ([date, temperature])

print(meteo)


