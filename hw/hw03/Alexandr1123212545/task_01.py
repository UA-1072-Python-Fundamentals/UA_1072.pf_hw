
def read_text(user_text: list):                         # function for counting occurrences of words
    word_1, word_2, word_3 = ['better', 'never', 'is']
    count_better, count_never, count_is = [0, 0, 0]
    calculate_dict = {}
    for line in user_text:
        count_better += line.split().count(word_1)
        count_never += line.split().count(word_2)
        count_is += line.split().count(word_3)
    print(f'\nТumber of occurrences: \nbetter - {count_better} \
          \nnever - {count_never} \nis - {count_is}\n')


def upper_all(user_text: list):                         # function for display uppercase text
    for line in user_text:
        print(line.upper(), end='')
    print('\n')


def replace_i(user_text: list):                        # function for replacin characters

    my_replace = str.maketrans("i", "&")
    for word in user_text:
        print(word.translate(my_replace), end='')
    print('\n')


with open('UA_1072.pf_hw\hw\hw03\Alexandr1123212545\zen.txt') as f:
    data = f.readlines()
    read_text(data)
    upper_all(data)
    replace_i(data)