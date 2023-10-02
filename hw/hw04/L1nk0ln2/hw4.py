celsiy = input("Введіть температуру в градусах Цельсію: ")

if float(celsiy) < -273.15:
    print("температура нижче абсолютного нуля (-273,15°C)")

else:
    convert = (float(celsiy) * (9 / 5)) + 32
    print("Температура в градусах Фаренгейту", round(convert, 1))
