#Menu Class
class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def calculate_bill(self, purchased_items):
        bill = 0
        for purchased_item in purchased_items:
            if purchased_item in self.items:
                bill += self.items[purchased_item]
        return bill

    def __repr__(self):
        return "The " + self.name + " is available from " + str(self.start_time) + ":00 - " + str(self.end_time) + ":00."

# Franchise Class
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return self.address

  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time > menu.start_time and time <= menu.end_time:  # Changed comparison for start time
        available_menus.append(menu)
    return available_menus


# Business Class
class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

# Brunch Menu Object
brunch_menu = Menu(
"Brunch",
    {'pancakes': 7.50,
        'waffles': 9.00,
            'burger': 11.00,
                'home fries': 4.50,
                    'coffee': 1.50,
                'espresso': 3.00,
            'tea': 1.00,
        'mimosa': 10.50,
        'orange juice': 3.50
    }, 11, 16)

# Early Bird Menu Object
early_bird_menu = Menu(
"Early Bird",
    {'salumeria plate': 8.00,
        'salad and breadsticks (serves 2, no refills)': 14.00,
            'pizza with quattro formaggi': 9.00,
                'duck ragu': 17.50,
                    'mushroom ravioli (vegan)': 13.50,
                'coffee': 1.50,
            'espresso': 3.00
        }, 15, 18)

# Dinner Menu Object
dinner_menu = Menu(
"Dinner",
    {'crostini with eggplant caponata': 13.00,
        'caesar salad': 16.00,
            'pizza with quattro formaggi': 11.00,
                'duck ragu': 19.50,
                    'mushroom ravioli (vegan)': 13.50,
                'coffee': 2.00,
            'espresso': 3.00 }, 17, 23)

# Kids Menu Object
kids_menu = Menu(
"Kids",
    {'chicken nuggets': 6.50,
            'fusilli with wild mushrooms': 12.00,
        'apple juice': 3.00
    }, 11, 21)

# All Menu's
menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]

# Flagship Store Object
flagship_store = Franchise("1232 West End Road", menus)

# New Installment Object
new_installment = Franchise("12 East Mulberry Street", menus)

# Basta Fazoolin Business Object
basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

# Arepa Items
arepas_items = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}

arepas_menu = Menu("Take a’ Arepas", arepas_items, 10, 16)

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

# arepa Fazoolin Business Object
arepa = Business("Take a' Arepa", [arepas_place, new_installment])

# Print Playground
print(brunch_menu.items)

print(flagship_store)

print(flagship_store.available_menus(17))

print(arepa.franchises[0].menus[0])

