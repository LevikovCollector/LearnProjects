
def compare_string (raw_first_str, raw_second_str):
	compare_result = None
	first_str = str(raw_first_str)
	second_str = str(raw_second_str)

	compare_result = None
	if first_str == second_str:
		compare_result = 1
	elif len(first_str) > len(second_str):
		compare_result = 2
	elif second_str == 'learn':
		compare_result = 3

	return compare_result


print(compare_string('история','история')) #1
print(compare_string(12,3)) # 2
print(compare_string(12,'learn')) #3
print(compare_string('история','learn')) #2