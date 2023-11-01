#Are you playing banjo?
def are_you_playing_banjo(name):
    if name.lower().startswith("r"):
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

#Convert boolean values to strings 'Yes' or 'No'
def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"

#Counting sheep
def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if i:
            count += 1
    return count

#OR!

def count_sheeps(sheep):
    return sheep.count(True)

#Is this my tail?
def correct_tail(body, tail):
    if tail == body[-1]:
        return True
    else:
        return False

#OR!

def correct_tail(body, tail):
    return body.endswith(tail)