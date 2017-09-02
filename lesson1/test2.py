def get_summ(one, two, delimeter = ' '):
	new_string = str(one) + str(delimeter) + str(two)
	return new_string.upper()

print(get_summ('Hello','World!', delimeter ='&'))
print(get_summ('Hello','World!', ' + '))
print(get_summ('Hello','World!'))
print(get_summ('Hello','World!', delimeter ='#'))