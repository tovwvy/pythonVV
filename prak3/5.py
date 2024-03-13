def determine_point_location(x, y):
    if x == 0 and y == 0:
        return "Точка знаходиться в початку координат."
    elif x == 0:
        return "Точка знаходиться на вісі Y."
    elif y == 0:
        return "Точка знаходиться на вісі X."
    elif x > 0 and y > 0:
        return "Точка знаходиться в першому квадранті."
    elif x < 0 and y > 0:
        return "Точка знаходиться в другому квадранті."
    elif x < 0 and y < 0:
        return "Точка знаходиться в третьому квадранті."
    else:
        return "Точка знаходиться в четвертому квадранті."

def main():
    x = float(input("Введіть координату x точки: "))
    y = float(input("Введіть координату y точки: "))
    location = determine_point_location(x, y)
    print(location)

if __name__ == "__main__":
    main()
