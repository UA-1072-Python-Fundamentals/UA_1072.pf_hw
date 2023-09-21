
def calculations(a, b, operation):
    if operation=='+':
        result= a+b
    elif operation=='-':
        result=a-b
    elif operation=='*':
        result=a*b
    elif operation=='/':
        result=a/b
    elif operation=='**':
        result=a**b
    elif operation=='//':
        result=a//b
    elif operation=='%':
        result=a%b
    return f' Your result = {result}'

a=float(input('What is a?'))
b=float(input('What is b?'))
operation=input('What is your operation +, -, *, /, //, %?')
result=calculations(a, b, operation)
print(result)
