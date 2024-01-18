# a simple app that will help the user to come up with a simple recipes from 3 simple ingredients.

# Display the list of ingredients
import random as rd

# make the list without the numbers but add the numbers to the output
ingredients_at_home = ["Tomato", "Cream", "Chicken", "Beef", "Bean", "Onion", "Bacon", "Mushroom", "Egg", "Mackarel"]
menu_order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# list of carbs and a carb randomiser for the final sentence
carb_list = ["pasta", "potatoes", "rice", "noodles", "soup", "omelette"]

# two of the ingredients are user inputs and one is a randomly selected ingredient for the final sentence
def random_food(ingredients_at_home):
    random_food = rd.choice(ingredients_at_home)
    return random_food

# customer input saved into a list
selected_ingredients = []

print("Welcome to Easy Cooking!")
print("Available ingredients:")
for num, food in zip(menu_order, ingredients_at_home):
    print(num,'-' , food) 

for j in range(2):
    choice = (input("Please pick an ingredient (1-10): "))
    
    # Check if the user's input is in the range
    if choice.isdigit() and 1 <= int(choice) <= 10:
        index = int(choice) - 1
        selected_ingredients.append(ingredients_at_home[int(choice) - 1]) 
    else:
        print("Invalid choice. Please enter a number between 1 and 10.")

# Display the selected ingredients
print("\nYour choices:")

for ingredient in selected_ingredients:
    print(ingredient) 

# Suggested dish based on the selected ingredients by using two user inputs, random carb and a random ingredient
random_carb = rd.choice(carb_list)
random_ingredient = rd.choice(ingredients_at_home)
user_ingredient = rd.choice(selected_ingredients)

#   
print(f"So how about {selected_ingredients[0]} {random_carb} with {selected_ingredients[1]} and {random_ingredient}?")



    



