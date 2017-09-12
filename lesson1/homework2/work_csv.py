import csv

answers = {'привет':'И тебе привет!', 'как дела':'Лучше всех', 'пока':'Увидимся'}

with open('answers.csv', 'w', encoding = 'utf-8') as answer_file:
    file_headers = ['keys', 'values']
    writer = csv.DictWriter(answer_file, file_headers, delimiter = ';')
    writer.writeheader()
    values_list = []
    values_dict = {}
    for key in answers.keys():
        values_dict['keys'] = key
        values_dict['values'] = answers[key]
        values_list.append(values_dict.copy())

    for row in values_list:
        writer.writerow(row)