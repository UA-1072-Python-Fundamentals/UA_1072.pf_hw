#Task2.1
number='2571'
product=int(number[0])*int(number[1])*int(number[2])*int(number[3])
print(product)

#Task2.2

#Solution1
number='2571'
print(number[::-1])

#Solution2
number='2571'
digits=list(number)
digits.reverse()
print(digits)

#Solution3
number='2571'
digits=list(number)
print(digits[::-1])

#Task2.3

#Solution1-the output with "[]"
number='2571'
print(sorted(number))

#Solution2-the output without "[]"
number='2571'
result=' '.join(sorted(number))
print(result)

