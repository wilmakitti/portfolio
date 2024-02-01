# Create a menu and list all the items you sell in the cafe
# Create a dictionary called stock and store a stock value of each item in it
# Create another dictionary called price, containing the price for each item on the menu

# Calculate the total_stock worth in the cafe. 
# Loop through the appropriate dictionaries and lists to do this

# At the last, print the sum of a total stock

print("Code Latte")

menu = ["Cinnamon Bun", "New York Cheese Cake", "Flat White", "Chai Latte", "Blueberry Pie", "Espresso Martini"]

def total_value(x):
    total = sum(v * stock[k] for k, v in price.items() if k in stock)
    return total_value

stock = {'Cinnamon Bun': 20,
        'New York Cheese Cake': 14,
        'Flat White': 40,
        'Chai Latte': 38,
        'Blueberry Pie': 19,
        'Espresso Martini': 15
        }

price = {'Cinnamon Bun': 3.5,
        'New York Cheese Cake': 7.5,
        'Flat White': 3.75,
        'Chai Latte': 3.75,
        'Blueberry Pie': 6.3,
        'Espresso Martini': 15.5
        }

print(price)
print(stock)

total_value = sum(v * stock[k] for k, v in price.items() if k in stock)

print("The total stock is: £",total_value)




















