def get_answer(question):
    try:
        answers = {'привет':'И тебе привет!', 'как дела':'Лучше всех', 'пока':'Увидимся'}
        return answers[str(question).lower()]
    except KeyError:
        return 'Нет никакого ответа!'
        
if __name__ == '__main__':
	get_answer('привет')