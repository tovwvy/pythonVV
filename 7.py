# Зчитування чисел a, b, c з клавіатури
a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))
c = int(input("Введіть число c: "))

# Підрахунок кількості негативних чисел
negative_count = 0
if a < 0:
  negative_count += 1
if b < 0:
  negative_count += 1
if c < 0:
  negative_count += 1

# Вивід результату
print("Кількість негативних чисел:", negative_count)
