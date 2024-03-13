def process_numbers():
    # Введення цілих чисел a та b з клавіатури
    a = int(input("Введіть ціле число a: "))
    b = int(input("Введіть ціле число b: "))

    # Порівняння чисел та заміна відповідно до умов
    if a != b:
        max_number = max(a, b)
        a = max_number
        b = max_number
    else:
        a = 0
        b = 0

    # Виведення результатів
    print("a =", a)
    print("b =", b)

# Виклик функції
process_numbers()
