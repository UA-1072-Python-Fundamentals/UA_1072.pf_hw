
def max_num(num1: int, num2: int) -> int:
  """Return the largest number.
  
  :param num1: first number
  :type num1: int
  :param num2: second number
  :type num2: int
  :return: sum of arguments
  :rtype: int
  """
  return max(num1, num2)

a, b = map(int, input('Enter the side parametrs siparated by a space \n').split())
print(max_num(a, b))
  
