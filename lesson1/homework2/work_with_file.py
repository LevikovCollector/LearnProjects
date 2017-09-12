with open('referat.txt','r', encoding = 'utf-8') as referat:
    file_words = 0
    for line in referat:
        read_str = line.replace('\n', '')
        words = read_str.split(' ')
        file_words += len(words)
    print('Слов в тексте: {0}'.format(file_words))
