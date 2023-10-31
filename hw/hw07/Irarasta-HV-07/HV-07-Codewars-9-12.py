

"""Here are Codewars tasks"""

  ## 9 -Are you playing Banjo?
def are_you_playing_banjo(name):
    if name.startswith('R') or name.startswith('r'):
        return name + " plays banjo."
    else:
        return name + " does not play banjo."
name = input("Enter a name: ")
result = are_you_playing_banjo(name)
print(result)



  ## 10- Convert boolean values to strings 'Yes' or 'No'.
def bool_to_word(boolean):
    if boolean:
        return 'Yes'
    else:
        return 'NO'




  ## 11- Counting sheep
def count_sheeps(sheep):
  return sheep.count(True)
sheep_list = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
result = count_sheeps(sheep_list)
print(result)



  ## 12- Is this my tail?
def correct_tail(body, tail):
    sub = body[-len(tail):]
    return sub == tail










