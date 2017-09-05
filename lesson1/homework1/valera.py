names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]

def find_person(name):
	while len(names) > 0:
		if  names.pop(0) == name:
			print( name + ' нашелся')
			break
	else:
		print( name + ' не нашелся')
		
find_person('Саша')
find_person('Кирилл')
	
	


