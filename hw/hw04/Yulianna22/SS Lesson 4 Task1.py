def c_temp (celsius):
    fahrenheit=(celsius*9/5)+32
    return(fahrenheit)
user_celsius=float(input('Enter the temperature in Celsius:'))
if user_celsius>-273.15:
    user_fahrenheit=c_temp(user_celsius)
    print(f'{user_celsius} is equivalent to {user_fahrenheit}')
elif user_celsius<=-273.15:
    print('Error: Temperature below absolute zero (-273.15°C)')
