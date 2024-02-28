# Вираз 1: Істине значення
var_1 = False
var_2 = 10 > 5

result_1 = var_1 or var_2

print("Вираз 1:", result_1)

# Вираз 2: Істине значення
var_3 = "a" not in "apple"
var_4 = 5 <= 5

result_2 = var_3 or var_4

print("Вираз 2:", result_2)

# Вираз 3: Хибне значення
var_5 = False
var_6 = "banana" == "apple"

result_3 = var_5 or var_6

print("Вираз 3:", result_3)

# Вираз 4: Хибне значення
var_7 = 10 < 5
var_8 = " " == ""

result_4 = var_7 or var_8

print("Вираз 4:", result_4)
