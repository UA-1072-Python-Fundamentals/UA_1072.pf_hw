

"""Here are Codewars tasks"""

  ## 5- Reverse string
def reverse(st):

    words = [word for word in st.split() if word]
    reverse_string = ' '.join(words[::-1])
    return reverse_string

input_string1 = "Hello World"
input_string2 = "Hi there"
output_string1 = reverse(input_string1)
output_string2 = reverse(input_string2)
print(output_string1)
print(output_string2)



  ## 6- Reverse list order
def reverse_list(list):
    list.reverse()
    return list
list = [1,2,3,4]
reversed_list = reverse_list(list)
print(reversed_list)



  ## 7- Multiple of 3 or 5
def solution(number):
    if number < 0:
        return 0

    total = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total += i

    return total
result = solution(54)
print(result)



  ## 8 -Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if fuel_left >= distance_to_pump / mpg:
        return True
    else:
        return False
result = zero_fuel(50, 25, 2)
print(result)












