# No yelling!

def filter_words(st):
    return ' '.join(st.split()).capitalize()

if __name__ == "__main__":
    print(filter_words('HELLO CAN YOU HEAR ME'))            # Hello can you hear me
    print(filter_words('now THIS is REALLY interesting'))   # Now this is really interesting
    print(filter_words('THAT was EXTRAORDINARY!'))          # That was extraordinary!
    print(filter_words('This    will    not    pass '))     # This will not pass