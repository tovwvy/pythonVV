def is_triangle_possible(angle1, angle2):
    # Сума кутів повинна дорівнювати 180 градусів
    sum_of_angles = angle1 + angle2 + 90  # Ураховуємо, що один з кутів може бути прямим
    return sum_of_angles == 180

def is_right_triangle(angle1, angle2):
    # Перевіряємо, чи один з кутів дорівнює 90 градусів
    return angle1 == 90 or angle2 == 90

# Зчитуємо величини кутів трикутника з клавіатури
angle1 = float(input("Введіть величину першого кута трикутника в градусах: "))
angle2 = float(input("Введіть величину другого кута трикутника в градусах: "))

# Перевіряємо, чи може існувати такий трикутник
if is_triangle_possible(angle1, angle2):
    if is_right_triangle(angle1, angle2):
        print("Такий трикутник існує і є прямокутним.")
    else:
        print("Такий трикутник існує, але він не є прямокутним.")
else:
    print("Такого трикутника не існує.")
