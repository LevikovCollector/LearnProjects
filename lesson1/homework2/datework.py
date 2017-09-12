from datetime import datetime, timedelta

deltaDay = timedelta(days = 1)
deltaMonth = timedelta(days = 31)

today = datetime.now()
yesterday = today - deltaDay
lastMonth = today - deltaMonth
print(today.strftime('%d.%m.%Y'))
print(yesterday.strftime('%d.%m.%Y'))
print(lastMonth.strftime('%d.%m.%Y'))



another_date = '01/01/17 12:10:03.234567'
date_for_convertion = datetime.strptime(another_date, '%d/%m/%y %H:%M:%S.%f')
print(type(date_for_convertion))
print(date_for_convertion)