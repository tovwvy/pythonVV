def count_integers(a, b, c):
    count = 0  # Ініціалізуємо лічильник цілих чисел

    # Перевіряємо кожне введене число на цілість
    if isinstance(a, int):
        count += 1
    if isinstance(b, int):
        count += 1
    if isinstance(c, int):
        count += 1

    return count

# Зчитуємо числа a, b і c з клавіатури
a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))
c = int(input("Введіть число c: "))

# Викликаємо функцію для підрахунку кількості цілих чисел
result = count_integers(a, b, c)
print("Кількість цілих чисел серед введених: ", result)
