def calculate_powers():
    # Зчитуємо три дійсних числа з клавіатури
    numbers = [float(input(f"Введіть {i+1}-е число: ")) for i in range(3)]
    
    # Підносимо до квадрата та четвертої ступеня
    powered_numbers = []
    for num in numbers:
        if num >= 0:
            powered_numbers.append(num ** 2)  # Підносимо до квадрата, якщо число невід'ємне
        else:
            powered_numbers.append(num ** 4)  # Підносимо до четвертої ступеня, якщо число від'ємне
    
    # Виводимо результат
    for i, num in enumerate(powered_numbers):
        print(f"Число {numbers[i]} піднесене до потрібного степеня: {num}")

calculate_powers()
