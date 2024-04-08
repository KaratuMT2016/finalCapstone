'''
This is a python program that takes stock inventory of a cafe based on a menu
• START
• Create a list with four menu items 
• Create a dictionary with the stock quantity of each menu
• Create a dictionary with the unit price of each menu item in the list
• From the cafe stock take the value of each stock item
• From the cafe price take the value of each price item
• Calculate the total stock of each menu
• Print the total stock of each menu 
• Calculate the overall total stock 
• print the overall total stock
• END
'''
cafe_menu = ["chicken and chips", "Rice Puddin", "Lasagne", "Maccaroni Cheese"]

cafe_stock = {"chicken and chips": 100,
              "Rice Puddin": 120,
              "Lasagne": 15,
              "Maccaroni Cheese": 80
            }

cafe_price = {"chicken and chips": 10.75,
              "Rice Puddin": 2.00,
              "Lasagne": 6.50,
              "Maccaroni Cheese": 8.50
            }


cafe_stock_values = cafe_stock.values() # Takes all the values of the stock from cafe_stock dictionary
cafe_price_values = cafe_price.values() # Takes all the values of the price from cafe_price dictionary


# Calculate the total stock for each menu item using a list comprehension
total_stock_for_each_menu = [stock * price for stock, price in zip(cafe_stock_values, cafe_price_values)]

print("Total stock for each menu item:", total_stock_for_each_menu)

# initialize total_stock

total_stock = 0.0

# Iterate throught the total_stock_for_each_menu and sum the total items
for item in total_stock_for_each_menu:
    total_stock += item

print("The total stock is:", total_stock)

#===========================================A more efficient version==========================================================


# Calculate the total stock for each menu item using a list comprehension
total_stock_for_each_menu = [cafe_stock[item] * cafe_price[item] for item in cafe_menu] # The cafe_menu list is not redundant

print("Total stock for each menu item:", total_stock_for_each_menu)

# Calculate the overall total stock using the sum function 
total_stock = sum(total_stock_for_each_menu) # Here the for loop is eliminated 

print("The total stock is:", total_stock)
