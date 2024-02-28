def zodiac_sign(year):
  """
  Функція для визначення знаку зодіаку за роком.

  Args:
    year: Ціле число, що відповідає року.

  Returns:
    Рядок, що описує знак зодіаку.
  """
  signs = ["Овен", "Телець", "Близнюки", "Рак", "Лев", "Діва", "Терези", "Скорпіон", "Стрілець", "Козеріг", "Водолій", "Риби"]
  start_years = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
  
  for i in range(len(signs)):
    if year >= start_years[i] and year < start_years[i + 1]:
      return signs[i]

year = int(input("Введіть рік: "))
sign = zodiac_sign(year)
print(f"Ваш знак зодіаку: {sign}")
