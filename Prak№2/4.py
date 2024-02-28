# Вираз 1: Істине значення
var_str1 = "apple"
var_str2 = "banana"

result_1 = var_str1 in var_str2

print("Вираз 1:", result_1)

# Вираз 2: Хибне значення
var_str3 = "orange"
var_str4 = "apple"

result_2 = var_str3 not in var_str4

print("Вираз 2:", result_2)

# Вираз 3: Істине значення
var_str5 = "pineapple"
var_str6 = "pineapple"

result_3 = var_str5 == var_str6

print("Вираз 3:", result_3)

# Вираз 4: Хибне значення
var_str7 = "mango"
var_str8 = "papaya"

result_4 = var_str7 != var_str8

print("Вираз 4:", result_4)
