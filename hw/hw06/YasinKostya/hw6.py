# TASK 6-1
def categorize_numbers():
  even_div_by_2 = [x for x in range(1, 11) if x % 2 == 0 and x % 4 == 0]
  odd_div_by_3 = [x for x in range(1, 11) if x % 2 != 0 and x % 3 == 0]
  not_div_by_2_and_3 = [x for x in range(1, 11) if x % 2 != 0 and x % 3 != 0]

  print("Even numbers divisible by 2:", even_div_by_2)
  print("Odd numbers divisible by 3:", odd_div_by_3)
  print("Numbers not divisible by 2 and 3:", not_div_by_2_and_3)


categorize_numbers()

# TASK 6-2
while True:
  login = str(input("Enter login\n"))
  if login == "Перший":
    print("Вітаємо, користувачу!")
    break
  else:
    print("Помилка: Невірний логін. Спробуйте ще раз.")