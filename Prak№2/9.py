def fibonacci(n):
  """
  Функція для обчислення n-го числа Фібоначчі.

  Args:
    n: Ціле число, що відповідає порядковому номеру числа Фібоначчі.

  Returns:
    Ціле число, що відповідає n-ому числу Фібоначчі.
  """
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

n = 20
fib_list = []
for i in range(n):
  fib_list.append(fibonacci(i))

print(f"Перші {n} чисел Фібоначчі:")
print(*fib_list)

# Виведення:
# Перші 20 чисел Фібоначчі:
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181
