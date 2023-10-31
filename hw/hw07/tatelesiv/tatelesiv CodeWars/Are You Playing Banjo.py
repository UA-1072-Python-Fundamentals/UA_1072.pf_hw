def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"


name1 = "Robert"
name2 = "Alice"

result1 = are_you_playing_banjo(name1)
result2 = are_you_playing_banjo(name2)

print(result1)
print(result2)
