def read_integers():
    
  a = int(input("Введіть число a: "))
  b = int(input("Введіть число b: "))
  c = int(input("Введіть число c: "))
  return a, b, c

def count_positives(a, b, c):
  """
  Функція підраховує кількість додатних чисел.
  """
  positive_count = 0
  if a > 0:
    positive_count += 1
  if b > 0:
    positive_count += 1
  if c > 0:
    positive_count += 1
  return positive_count

def print_results(positive_count):
  """
  Функція виводить результат.
  """
  print("Кількість додатних чисел:", positive_count)

# Виклик функцій
a, b, c = read_integers()
positive_count = count_positives(a, b, c)
print_results(positive_count)
