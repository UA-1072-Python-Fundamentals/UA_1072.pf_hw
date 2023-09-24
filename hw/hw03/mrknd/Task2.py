num = 4321

#Task2.1
product = int(num // 1000) * int((num // 100) % 10) * int((num // 10) % 10) * int(num % 10)
print("Product:", product)

#Task2.2
reverse_num = int(str(num)[::-1])
print("Reverse:", reverse_num)

#Task2.3
sort_num = "".join(sorted(str(num)))
print("Sorted numbers:", sort_num)

