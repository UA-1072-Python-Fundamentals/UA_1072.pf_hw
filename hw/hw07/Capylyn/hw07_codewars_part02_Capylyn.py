#Reversing Words in a String
def reverse(st):
    st = st.split()
    st.reverse()
    return " ".join(st)

#Reverse List Order
def reverse_list(l):
    return l[::-1]

#Multiples of 3 or 5
def solution(number):
    if number < 0:
        return 0
    l = []
    for i in range(number):
        if not i % 3 or not i % 5:
            l.append(i)

    return sum(l)

#Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg * fuel_left >= distance_to_pump:
        return True
    else:
        return False