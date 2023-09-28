def converter_t(value: float):    
  if value < -273.15:
    print('Error:Temperature below absolute zero (-273.15°C)')
  else:
    result = round((value * (9 / 5) + 32), 2) # Сonversion from Celsius to Fahrenheit
    print(f'{value}{chr(176)}C is equivalent to {result}{chr(176)}F')


user_t = float(input('Enter the temperature in Celsius '))
result = converter_t(user_t)