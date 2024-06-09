Restaurant Menu Manager with Franchises (Python)
  
This Python code implements a program to manage menus, franchises, and functionalities for a restaurant business.


- Features
  
Menu Class: Represents a menu with a name, available items (including prices), start and end times.

Franchise Class: Represents a franchise location with an address and a list of associated menus.

Business Class: Represents a restaurant business with a name and a list of franchises.

Bill Calculation: Calculates the total bill based on purchased items and their corresponding prices in the menu.

Available Menus: Determines which menus are available based on a given time.


- Usage
  
The code is primarily for demonstration purposes, but it can be used as a starting point for building a restaurant menu management system.

Here's a breakdown of the -

functionalities:

Creating Menus:

Define a dictionary containing menu items as keys and their prices as values.

Use the Menu class constructor to create a menu object with a name, items dictionary, start time, and end time.

Creating Franchises:

Specify the franchise address.

Create a list of menu objects associated with the franchise.

Use the Franchise class constructor to create a franchise object with the address and list of menus.

Creating a Business:

Define the business name.

Create a list of franchise objects.

Use the Business class constructor to create a business object with the name and list of franchises.

Calculating Bills:

Provide a list of purchased items from a specific menu.

The calculate_bill method of the Menu class iterates through the purchased items and retrieves their prices from the menu's items dictionary.

Checking Available Menus:

Pass a time (in hours) as an argument to the available_menus method of the Franchise class.

This method iterates through the franchise's menus and checks if the time falls within the start and end times of each menu. 

It returns a list of available menus at that time.


- Testing

The provided code includes a basic print playground at the end. You can run the script to:

View the items in a specific menu (print(brunch_menu.items))

See the information of a franchise (print(flagship_store))

Check available menus at a particular time 
(print(flagship_store.available_menus(17)))

Access a menu of another franchise (print(arepa.franchises[0].menus[0]))

To further test the functionalities, you can modify the data (menu items, prices, times) and experiment with different scenarios.

You can also write your own unit tests to ensure the code behaves as expected.


- Dependencies
This code requires no external libraries beyond Python's built-in functionalities.


- Free Use!

 Feel free to adapt and extend it for your specific needs!
