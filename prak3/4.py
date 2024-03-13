def replace_numbers(x, y):
    # Перевіряємо, яке з чисел менше
    if x < y:
        # Замінюємо менше число половиною їх суми
        x = (x + y) / 2
        # Замінюємо більше число їх подвоєним добутком
        y = 2 * x
    else:
        # Замінюємо менше число половиною їх суми
        y = (x + y) / 2
        # Замінюємо більше число їх подвоєним добутком
        x = 2 * y
    
    # Повертаємо замінені значення
    return x, y

# Зчитуємо дійсні числа x і y з клавіатури
x = float(input("Введіть число x: "))
y = float(input("Введіть число y: "))

# Викликаємо функцію replace_numbers з введеними значеннями x і y
new_x, new_y = replace_numbers(x, y)

# Виводимо результат
print("Менше число замінене на", new_x)
print("Більше число замінене на", new_y)
