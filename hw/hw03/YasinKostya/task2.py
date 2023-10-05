digit = int(input("Enter a four-digit natural number: "))


dobutok = int(digit // 1000) * int((digit // 100) % 10) * int((digit // 10) % 10) * int(digit % 10)
print(f"Dobutik {dobutok}")

digit_reverse = int(str(digit)[::-1])
print(f"Reverse digit = {digit_reverse}")

sorted_digit = int(''.join(sorted(str(digit))))
print(f"Sorted digit = {sorted_digit}")