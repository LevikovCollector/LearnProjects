from answers import get_answer

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


   


ask_user()