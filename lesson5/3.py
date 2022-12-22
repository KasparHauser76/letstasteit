def adder(*args):
  """суммирование множества вводимых аргументов, в том числе и 0"""
  sum = 0
  for i in args:
    sum += i
  return sum
print(adder(0, 1, 2, 3, 5, 10))