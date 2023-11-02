def filter_words(phrase):
    new_phrase=" ".join(phrase.split())
    print(new_phrase.capitalize())

filter_words(input("Input any phrase: "))