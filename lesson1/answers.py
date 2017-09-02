def get_answer(question):
    answers = {'привет':'И тебе привет!', 'как дела':'Лучше всех', 'пока':'Увидимся'}
    #return answers[question.lower()]
    return answers.get(str(question).lower(), 'Моя твоя не понимать')   

print(get_answer('привет'))
print(get_answer('как дела'))
print(get_answer('пока'))
print(get_answer(111))
print(get_answer('Привет'))
print(get_answer('Как дела'))
print(get_answer('покА'))
    
    