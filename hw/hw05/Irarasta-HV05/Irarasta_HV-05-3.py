  ## Write a script, that will calculate the factorial of the
  ## entered number, without using recursion

factorial = int(input('Enter any Positive Number for Factorial calculation: '))
if factorial <= 0:
    print('NO Factorial calculation for ZERO or Negative Number! '
          'Give a Positive Number, please!')
else:
    def def_factorial(n):
        if n == 0:
            return 1
        else:
            result = 1
            for i in range(1, n + 1):
                result *= i
            return result
    result = def_factorial(factorial)
    print(f'The factorial of {factorial} is {result}')





