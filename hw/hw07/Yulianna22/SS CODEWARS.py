#Jenny's secret message
def jenny_message(user_name):
    if user_name=='Johnny':
        return f'Hello, {user_name}, you are my love!'
    else:
        return f'Hello,{user_name}, welcome to us!'
    
#Find The Distance Between Two Points
def distance(x1,x2,y1,y2):
    result=((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return round(result,2)

#No yelling
def corrected_string(string):
    string=' '.join(string.split())
    return string.capitalize()

#Convert a Number to a String
def number_into_string(number):
    number=str(number)
    return number

#Reversing Words in a String
def reversed_words(string):
    result=' '.join(string.split()[::-1])
    return result

#Reverse List Order
def reversed_list_order(list):
    list.reverse()
    return list

#Multiples of 3 or 5
def multiples_3_5(number):
    number=int(number)
    list=[]
    if number<0:
        return 0
    for i in range(number):
        if i%3==0:
            list.append(i)
        elif i%5==0:
            list.append(i)
        elif i%3!=0 or i%5!=0:
            continue
    result=sum(list)
    return result

# Will you make it?
def get_to_pump(distance, mpg, gallons_left):
    mpg=25
    if distance/mpg<=gallons_left:
        return True
    else:
        return False
    
#user_distance=float(input('Distance to the pump?'))
#user_gallons_left=float(input('How many gallons are left?'))
#result=get_to_pump(user_distance,25,user_gallons_left)
#print(result)

#Are You Playing Banjo?
def banjo_player(name):
    for i in name:
        if i[0]=='R' or i[0]=='r':
            return name + " plays banjo" 
        else:
            return name + " does not play banjo"
        
#user_name=input('What`s your name?')
#result=banjo_player(user_name)
#print(result)

#Convert boolean values to strings 'Yes' or 'No'
def boolean_into_string(boolean_value):
    if boolean_value=='True':
        return 'Yes'
    elif boolean_value=='False':
        return 'No'
    
#user_value=input('Your value?')
#result=boolean_into_string(user_value)
#print(result)

#Counting sheep...
def count_sheep(sheep):
    counter=0
    for s in sheep:
        if s is True:
            counter+=1
    return counter

#sheep=[True,  True,  True,  False, True,  True,  True,  True , True,  False, True,  False, True,  False, False, True , True,  True,  True,  True , False, False, True,  True]
#result=count_sheep(sheep)
#print(f'There are {result} sheep')

#Is this my tail?
def correct_tail (body,tail):
        if body [-1]==tail:
            return True
        else:
            return False
#user_body=input('What`s the body?')
#user_tail=input('What`s the tail')
#result=correct_tail(user_body, user_tail)
#print(result)