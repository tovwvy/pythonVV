# Зчитування чисел a, b, c з клавіатури
a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))
c = int(input("Введіть число c: "))

# Підрахунок кількості цілих чисел
integer_count = 0
if a.is_integer():
  integer_count += 1
if b.is_integer():
  integer_count += 1
if c.is_integer():
  integer_count += 1

# Вивід результату
print("Кількість цілих чисел:", integer_count)
