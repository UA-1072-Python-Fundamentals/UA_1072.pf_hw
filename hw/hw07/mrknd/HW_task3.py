def calculates(word):
    count_letters = {}
    for i in word:
        if i in count_letters:
            count_letters[i] += 1
        else:
            count_letters[i] = 1
    return count_letters


ask = input('Enter a word and I will count the letters: ')
print(calculates(ask))