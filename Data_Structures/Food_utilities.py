"""
-------------------------------------------------------
Food class utility functions.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2023-05-15"
-------------------------------------------------------
"""
from Food import Food
from copy import deepcopy


def get_food():
    """
    -------------------------------------------------------
    Creates a Food object by requesting data from a user.
    Use: source = get_food()
    -------------------------------------------------------
    Returns:
        food - a completed food object (Food).
    -------------------------------------------------------
    """
    name = input("Enter the food name: ")
    print(Food.origins())
    
    # Input validation for origin_id
    while True:
        try:
            origin_id = int(input("Enter the origin ID: "))
            if 0 <= origin_id < len(Food.ORIGIN):
                break
            else:
                print("Invalid origin ID. Please choose a valid ID.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for origin ID.")
    
    is_vegetarian_str = input("Is the food vegetarian? (yes/no): ").lower()
    
    # Consistent spelling for vegetarian input
    is_vegetarian = is_vegetarian_str == 'yes'
    
    # Input validation for calories_input
    while True:
        calories_input = input("Enter the caloric content (press enter for not specified): ")
        if calories_input == '':
            calories = None
            break
        try:
            calories = int(calories_input)
            if calories >= 0:
                break
            else:
                print("Calories must be a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for calories.")
    
    food = Food(name, origin_id, is_vegetarian, calories)
    
    return food


def read_food(line):
    """
    -------------------------------------------------------
    Creates and returns a Food object from a line of string data.
    Use: source = read_food(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of food data in the format
          name|origin|is_vegetarian|calories (str)
    Returns:
        food - contains the data from line (Food)
    -------------------------------------------------------
    """

    components = line.strip().split('|')
    name = components[0]
    origin = int(components[1])
    is_vegetarian = components[2].lower() == 'true'
    calories = int(components[3]) 
    food = Food(name, origin, is_vegetarian, calories)

    return food


def read_foods(file_variable):
    """
    -------------------------------------------------------
    Reads a file of food strings into a list of Food objects.
    Use: foods = read_foods(file_variable)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
    Returns:
        foods - a list of food objects (list of Food)
    -------------------------------------------------------
    """
    lines = file_variable.readlines()
    foods = []
    for line in lines:
        food = read_food(line)
        foods.append(food)
    

    return foods


def write_foods(file_variable, foods):
    """
    -------------------------------------------------------
    Writes a list of Food objects to a file.
    file_variable contains the objects in foods as strings in the format
          name|origin|is_vegetarian|calories
    foods is unchanged.
    Use: write_foods(file_variable, foods)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file variable)
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """
    for food in foods:
        line = f"{food.name}|{food.origin}|{food.is_vegetarian}|{food.calories}\n"
        file_variable.write(line)

    return


def get_vegetarian(foods):
    """
    -------------------------------------------------------
    Creates a list of vegetarian Food objects.
    foods is unchanged.
    Use: v_foods = get_vegetarian(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        veggies - Food objects from foods that are vegetarian (list of Food)
    -------------------------------------------------------
    """

    veggies = [food for food in foods if food.is_vegetarian]

    return veggies


def by_origin(foods, origin):
    """
    -------------------------------------------------------
    Creates a list of Food objects by origin.
    foods is unchanged.
    Use: o_foods = by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - a food origin (int)
    Returns:
        origins - Food objects from foods that are of a particular origin (list of Food)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))
    origins = [food for food in foods if food.origin == origin]

    return origins


def average_calories(foods):
    """
    -------------------------------------------------------
    Determines the average calories in a list of Foods objects.
    foods is unchanged.
    Use: avg = average_calories(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        avg - average calories in all Food objects of foods (int)
    -------------------------------------------------------
    """

    total_calories = sum(food.calories for food in foods if food.calories is not None)
    num_food_objects = len([food for food in foods if food.calories is not None])
    avg = total_calories / num_food_objects if num_food_objects > 0 else 0
    
    return avg


def calories_by_origin(foods, origin):
    """
    -------------------------------------------------------
    Determines the average calories in a list of Foods objects.
    foods is unchanged.
    Use: by_origin = calories_by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the Food objects to find (int)
    Returns:
        avg - average calories for all Foods of the requested origin (int)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))
    filtered_foods = [food for food in foods if food.origin == origin]
    total_calories = sum(food.calories for food in filtered_foods if food.calories is not None)
    num_food_objects = len([food for food in filtered_foods if food.calories is not None])
    avg = total_calories/ num_food_objects if num_food_objects > 0 else 0 


    return avg


def food_table(foods):
    """
    -------------------------------------------------------
    Prints a formatted table of Food objects, sorted by name.
    foods is unchanged.
    Use: food_table(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """
    sorted_foods = sorted(foods, key=lambda food: food.name)

    
    print("{:<35} {:<15} {:<15} {:<10}".format("Food", "Origin", "Vegetarian", "Calories"))
    print("{:<35} {:<15} {:<15} {:<10}".format("--------------------------------- ", "--------------", "--------------", "--------"))

    for food in sorted_foods:
        origin_name = Food.ORIGIN[food.origin]
        is_vegetarian = "Yes" if food.is_vegetarian else "No"
        calories = str(food.calories) if food.calories is not None else "N/A"

        print("{:<35} {:<15} {:<15} {:<10}".format(food.name, origin_name, is_vegetarian, calories))

    return

   


def food_search(foods, origin, max_cals, is_veg):
    """
    -------------------------------------------------------
    Searches for Food objects that fit certain conditions.
    foods is unchanged.
    Use: results = food_search(foods, origin, max_cals, is_veg)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the food; if -1, accept any origin (int)
        max_cals - the maximum calories for the food; if 0, accept any calories value (int)
        is_veg - whether the food is vegetarian or not; if False accept any food (boolean)
    Returns:
        result - a list of foods that fit the conditions (list of Food)
            foods parameter must be unchanged
    -------------------------------------------------------
    """

    assert origin in range(-1, len(Food.ORIGIN))

    food_2 = deepcopy(foods)
    
    
    result = [food for food in food_2 if  (origin == -1 or food.origin == origin) \
              and (max_cals == 0 or food.calories <= max_cals) \
              and (not is_veg or food.is_vegetarian == is_veg)]

    return result

