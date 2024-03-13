def read_integers():
  
  a = int(input("Введіть число a: "))
  b = int(input("Введіть число b: "))
  c = int(input("Введіть число c: "))
  k = int(input("Введіть число k: "))
  return a, b, c, k

def check_divisibility(a, b, c, k):
  """
  Функція перевіряє, чи є k дільником a, b, c.
  """
  divisible_by_a = (a % k == 0)
  divisible_by_b = (b % k == 0)
  divisible_by_c = (c % k == 0)
  return divisible_by_a, divisible_by_b, divisible_by_c

def print_results(divisible_by_a, divisible_by_b, divisible_by_c):
  """
  Функція виводить результат.
  """
  print("Число k є дільником:")
  if divisible_by_a:
    print("a")
  if divisible_by_b:
    print("b")
  if divisible_by_c:
    print("c")

  if not (divisible_by_a or divisible_by_b or divisible_by_c):
    print("жодного з чисел a, b, c")

# Виклик функцій
a, b, c, k = read_integers()
divisible_by_a, divisible_by_b, divisible_by_c = check_divisibility(a, b, c, k)
print_results(divisible_by_a, divisible_by_b, divisible_by_c)
