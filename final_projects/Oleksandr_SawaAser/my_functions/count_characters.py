__all__ = ['count_characters']


def count_characters(text):
    sorted_list = []
    for character in set(text.lower()):
        sorted_list.append([character, text.lower().count(character)])
    for i in range(len(sorted_list)):
        for j in range(len(sorted_list)-1):
            if sorted_list[j][1] < sorted_list[j+1][1]:
                sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
    return sorted_list
