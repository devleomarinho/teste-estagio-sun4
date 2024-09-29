def q2_contar_frequencia_palavra(text):

    word_list = text.lower().split(' ')
    word_count = {}
    for word in word_list:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count

print(q2_contar_frequencia_palavra("Hello world hello"))
