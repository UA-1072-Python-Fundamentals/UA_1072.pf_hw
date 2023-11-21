#Калькулятор для вичеслення пропорцій при виготовленні моделей з гіпсу.
def вичислити_пропорції(відношення, кількість_води):
    кількість_порошку = відношення * кількість_води
    return кількість_порошку, кількість_води

# Введіть відношення порошку до води, яке вказане на упаковці гіпсу
відношення_порошку_до_води = 100 / 30  # Наприклад, 100 г порошку на 30 мл води

кількість_води = float(input('Введіть кількість води (мл): '))

кількість_порошку, використана_вода = вичислити_пропорції(відношення_порошку_до_води, кількість_води)

print(f'Кількість порошку: {кількість_порошку} г')
print(f'Кількість використаної води: {використана_вода} мл')