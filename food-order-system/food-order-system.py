italian_food = ["Pasta Bolognese", "Pepperoni pizza", "Margherita pizza", "Lasagna"]
indian_food = ["Curry", "Chutney", "Samosa", "Naan"]

def find_meal(name, menu):
    if name in menu:
        return name
    else:
        return None

def select_meal(name, food_type):
    if food_type == "Italian":
        return find_meal(name, italian_food)
    elif food_type == "Indian":
        return find_meal(name, indian_food)
    else:
        return None

def display_available_meals(food_type):
    if food_type == "Italian":
        print("Available Italian Meals:")
        for food in italian_food:
            print(f"- {food}")
    elif food_type == "Indian":
        print("Available Indian Meals:")
        for food in indian_food:
            print(f"- {food}")
    else:
        print("Invalid food type")

def create_summary(name, amount, food_type):  # ✅ Added food_type here
    order = select_meal(name, food_type)      # ✅ Pass food_type into select_meal
    if order:
        return f"You ordered {amount} x {order}."
    else:
        return "Sorry, that meal is not available."

# Program start
print("Welcome to the Food Order System!")

type_input = input("What type of food would you like? (Italian or Indian): ")
display_available_meals(type_input)

name_input = input("Meal Choice: ")
amount_input = input("Order Quantity: ")

# ✅ Pass type_input as food_type
result = create_summary(name_input, amount_input, type_input)
print(result)

