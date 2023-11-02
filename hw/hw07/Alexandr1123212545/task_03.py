
def amount(text: str) -> dict:
  """Number of each element in the string.

  :param text: test text 'hello'
  :type text: str
  :return: count of each element in the string
  :rtype: dict
  """
  return  dict(map(lambda x: (x, text.count(x)), text)) 

print(amount('hello'))
