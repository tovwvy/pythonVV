# Зчитування чисел a, b, c, k з клавіатури
a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))
c = int(input("Введіть число c: "))
k = int(input("Введіть число k: "))

# Перевірка, чи є k дільником a, b, c
divisible_by_a = (a % k == 0)
divisible_by_b = (b % k == 0)
divisible_by_c = (c % k == 0)

# Вивід результату
print("Число k є дільником:")
if divisible_by_a:
  print("a")
if divisible_by_b:
  print("b")
if divisible_by_c:
  print("c")

if not (divisible_by_a or divisible_by_b or divisible_by_c):
  print("жодного з чисел a, b, c")
