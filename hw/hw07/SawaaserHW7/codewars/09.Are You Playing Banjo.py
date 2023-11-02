def are_you_playing_banjo(name):
    name = name + ' plays banjo' if name[0] in "Rr" else name + ' does not play banjo'
    return name


print(are_you_playing_banjo("Rikke"))
