def reverse(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_string = ' '.join(reversed_words)

    return reversed_string


print(reverse("Hello World, How are you?"))
print(reverse("Hi There."))
