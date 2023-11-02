# Reversing Words in a String

def reverse(st):
    return ' '.join(st.split()[::-1])


if __name__ == "__main__":
    print(reverse('Hello World')) # World Hello
    print(reverse('Hi There.'))   # There. Hi