def read_integers():
   
  a = int(input("Введіть число a: "))
  b = int(input("Введіть число b: "))
  c = int(input("Введіть число c: "))
  return a, b, c

def count_negatives(a, b, c):
  """
  Функція підраховує кількість негативних чисел.
  """
  negative_count = 0
  if a < 0:
    negative_count += 1
  if b < 0:
    negative_count += 1
  if c < 0:
    negative_count += 1
  return negative_count

def print_results(negative_count):
  """
  Функція виводить результат.
  """
  print("Кількість негативних чисел:", negative_count)

# Виклик функцій
a, b, c = read_integers()
negative_count = count_negatives(a, b, c)
print_results(negative_count)
