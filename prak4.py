class With_land:
    def __init__(self):
        self.land_area = None

    def get_land_area(self):
        return self.land_area

    def set_land_area(self, land_area):
        self.land_area = land_area

    def __str__(self):
        return f"Будинок з земельною ділянкою"


class Without_land:
    def __str__(self):
        return f"Будинок без земельної ділянки"


class For_one_family(With_land):
    def __str__(self):
        return f"Будинок для однієї сім'ї (з земельною ділянкою)"


class For_many_families(Without_land):
    def __init__(self):
        self.number_of_families = None

    def get_number_of_families(self):
        return self.number_of_families

    def set_number_of_families(self, number_of_families):
        self.number_of_families = number_of_families

    def __str__(self):
        return f"Будинок для багатьох сімей (без земельної ділянки)"


class Villets(For_one_family):
    def __str__(self):
        return f"Вілла (будинок для однієї сім'ї з земельною ділянкою)"


class Apartments(For_many_families):
    def __str__(self):
        return f"Квартира (будинок для багатьох сімей без земельної ділянки)"


# Створення об'єктів
villet = Villets()
apartment = Apartments()

# Виклик обробників повідомлень
print(villet)
print(apartment)
