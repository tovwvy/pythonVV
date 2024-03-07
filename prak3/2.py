import math

def distance_to_origin(x, y):
    return math.sqrt(x ** 2 + y ** 2)

def closer_point_to_origin(x1, y1, x2, y2):
    distance_A = distance_to_origin(x1, y1)
    distance_B = distance_to_origin(x2, y2)
    
    if distance_A < distance_B:
        return "Точка A знаходиться ближче до початку координат."
    elif distance_A > distance_B:
        return "Точка B знаходиться ближче до початку координат."
    else:
        return "Точки A і B розташовані на однаковій відстані від початку координат."

# Зчитуємо координати точок з клавіатури
x1 = float(input("Введіть координату x для точки A: "))
y1 = float(input("Введіть координату y для точки A: "))
x2 = float(input("Введіть координату x для точки B: "))
y2 = float(input("Введіть координату y для точки B: "))

# Визначаємо, яка точка знаходиться ближче до початку координат
result = closer_point_to_origin(x1, y1, x2, y2)
print(result)
