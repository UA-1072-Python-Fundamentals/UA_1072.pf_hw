__all__ = ['count_words']


def count_words(text):
    bad_characters = '!@#$%^&*()_+=-<>?,./'
    for char in bad_characters:
        text = text.replace(char, '')
    sorted_list = []
    for character in set(text.lower().split()):
        sorted_list.append([character, len(list(filter(lambda x: x == character, list(text.lower().split()))))])
    for i in range(len(sorted_list)):
        for j in range(len(sorted_list)-1):
            if sorted_list[j][1] < sorted_list[j+1][1]:
                sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
    return sorted_list
