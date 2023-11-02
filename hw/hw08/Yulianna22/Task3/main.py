from functions import rectangle_area, triangle_area, circle_area

while True:
    user_choice=input('Choose a number of the figure you want to calculate:\nRectangle:1\nTriangle:2\nCircle:3\nYOUR CHOICE:')
    if user_choice=='1':
        user_a=float(input('What is the length of the rectangle?:'))
        user_b=float(input('What is the width of the rectangle?:'))
        result=rectangle_area(user_a,user_b)
        print(f'Your rectangle area is {result}')
        break
    elif user_choice=='2':
        user_height=float(input('What is the height if the rectangle?:'))
        user_base=float(input('What is the base of the rectangle?:'))
        result=triangle_area(user_height,user_base)
        print(f'Your triangle area is {result}')
        break
    elif user_choice=='3':
        user_radius=float(input('What is the radius?'))
        result=circle_area(user_radius)
        print(f'Your circle area is{result}')
        break
    else:
        print('Your input is invalid.')
        continue
print('See you next time!')



    
