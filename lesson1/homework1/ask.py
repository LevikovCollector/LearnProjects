

def ask_user():
    while True:
        try:
            answer = input ('Как дела ? \n')
            response = get_answer(answer)
            if (answer == 'Пока!' or answer == 'Пока'or answer == 'пока'):
                print(response)
                break
            else:
                print(response)
        except KeyboardInterrupt:
            print('До новых встреч!')
            break

def get_answer(question):
    try:
        answers = {'привет':'И тебе привет!', 'как дела':'Лучше всех', 'пока':'Увидимся'}
        return answers[str(question).lower()]
    except KeyError:
        return 'Нет никакого ответа!'
   


ask_user()