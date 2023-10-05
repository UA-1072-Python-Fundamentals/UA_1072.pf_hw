  ## Print Fibonacci numbers up to the entered number "n" using "cycles":
  ## Define the last number of the future sequence:

n = int(input('Define the last number for Fibonacci sequence: '))

  ## Define first TWO numbers to start the sequence
x, y, = 0, 1
print(x)
print(y)
  ##
while x + y <= n:
    fibonacci  = x + y
    print(fibonacci)
    x = y
    y = fibonacci

