spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    names = [food['name'] for food in spicy_foods]
    return names


def get_spiciest_foods(spicy_foods):
    if not spicy_foods:
        return []

    max_heat = -1
    spiciest = []
    for food in spicy_foods:
        if food['heat_level'] > max_heat:
            max_heat = food['heat_level']
            spiciest = [food]
        elif food['heat_level'] == max_heat:
            spiciest.append(food)
    return spiciest


def print_spicy_foods(spicy_foods):
    if not spicy_foods:
        return
    sorted_foods = sorted(spicy_foods, key=lambda food: food['name'])
    for food in sorted_foods:
        print(
            f"🌶️ {food['name']} ({food['cuisine']}) | Heat Level: {food['heat_level']}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    foods_of_cuisine = [
        food for food in spicy_foods if food['cuisine'] == cuisine]
    return foods_of_cuisine


def print_spiciest_foods(spicy_foods):
    if not spicy_foods:
        return

    max_heat = -1
    spiciest_foods_list = []
    for food in spicy_foods:
        if food['heat_level'] > max_heat:
            max_heat = food['heat_level']
            spiciest_foods_list = [food]
        elif food['heat_level'] == max_heat:
            spiciest_foods_list.append(food)

    for food in spiciest_foods_list:
        print(
            f"🌶️ {food['name']} ({food['cuisine']}) | Heat Level: {food['heat_level']}")


def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    return total_heat / len(spicy_foods)


def create_spicy_food(spicy_foods, spicy_food):
    new_spicy_foods = spicy_foods + [spicy_food]
    return new_spicy_foods
