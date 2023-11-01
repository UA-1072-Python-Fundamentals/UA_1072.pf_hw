C = float(input('Enter the temperature in Celsius: '))
if C >= -273.150:
    F = C * 9/5 + 32
    print(f'{C}°C is equivalent to {F}°F')
else:
    print('Temperature is below absolute zero (-273,150 °C)')