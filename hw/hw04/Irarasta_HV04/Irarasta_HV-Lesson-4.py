C = float(input('Enter the temperature in Celsius: '))
if C >= -273.15:
    F = C * 9/5 + 32
    print(f'{C}°C is equivalent {F}°F')
else:
    print('Temperature is below absolute ZERO (-273,15 °C)')

