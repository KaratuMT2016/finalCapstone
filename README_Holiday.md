"""
This is a python program that will calculate a user's total holiday cost, viz; the plane cost, hotel cost, and car-rental cost.
• START
• Create a Python file called holiday.py
• Create a class named Holiday
    • Initialise the class by defining a constructor __init__
    • Define __str__ function that will return default values for the __init__ arguemnts
    • Create the following dictionaries:
        •   city_flight_cost for the flight destinations
        •   hotel_price_list for the hotel room types
        •   car_rental_price_list for the car rental type, respectively.
    • Create static methods for the following variable to ensure only integer values are entered:
        •   num_nights
        •   rental_days
    • Define the following menus:
        •   Main menu()
        •   Hotel room types menu room_types_menu()
        •   Car rental types menu car_rental_menu()
    • Create text file to read from as follows:
        •   List of selected city destination to choose from
        •   List of hotel room types to choose from
        •   List of car rental types to choose from
    • Define the following functions to read the text file above
        •   destination_list() to read city flight destinations text file
        •   hotel_room_type_list() to read the hotel room types text file
        •   car_rental_list() to read the car rental types text file
    • Define the following methods to compute hotel, plane, and car rental cost from the respective dictionaries
        •   hotel_cost() method to compute hotel cost from the city_flight_cost dictionary
        •   plane_cost() method to compute flight cost from the hotel_price_list dictionary
        •   car_rental() method to compute rental cost from the car_rental_price_list dictionary
        •   holiday_cost() method to compute the total holiday cost
    •  From here the main program starts:
        •   Call the main menu()
        •   Input a user's flight destination
        •   Validate a users choice of destionation
        •   while user's input for a destination is True:
            •   Call the Hotel room types menu - room_types_menu()
            •   Input a user's choice of hotel room type
            •   Validate a user's choice of hotel room
            •   Input a user's number of nights to stay in the hotel room - this is validated using the @staticMethod - get_integer_num_nights()
            •   Call the car rental type menu - car_rental_menu()
            •   Input a user's choice of rental car
            •   Validate a user's choice of rental car
            •   Input a user's number of days for the rental - this is validated using the @staticMethod - get_integer_rental_days()
            •   Break out of the while loop
        •   Call an instance of the holiday cost menthod:
        •   Holiday.holiday_cost()
        •   print a Goodbye! message.
        •   End while loop
    •   End Holiday Class
END Program
"""
