import collections  # The defaultdict makes a special dictionary which adds a list as default, as the value of a new key
fruit = collections.defaultdict(list)
bread = collections.defaultdict(list)
dairy = collections.defaultdict(list)
misc = collections.defaultdict(list)
meat = collections.defaultdict(list)
sweets = collections.defaultdict(list)
household = collections.defaultdict(list)
frozen = collections.defaultdict(list)

category = ""  # Initialise the category
category_active = True  # Initialise a Boolean which is active when items are being added
request = ""  # Initialise an empty variable to be used in the while loop later on
for who in ["mom", "bette", "gaynor", "mel"]:  # list of shopping list owners
    print(f"LOOKING AT {who.upper()}'s SHOPPING LIST....")  # Introductory statement for whose shopping it is
    for category in ["fruit and veg", "dairy", "meat", "household", "bread", "sweets", "misc", "frozen"]:
        category_active = True  # Activate category so items can be added
        while category_active is True:  # Ask for items while the category is active
            request = input(f"What {category} stuff do they want? (Q to finish this category) - ")
            if request.lower() == "q":  # User enters q to switch categories
                category_active = False
                break  # Exits the while loop and asks for the next category
            # If the current category is x, then add the item to the value's list with the owner as the key
            if category.lower() == "fruit and veg":
                fruit[who].append(request)
            elif category.lower() == "bread":
                bread[who].append(request)
            elif category.lower() == "dairy":
                dairy[who].append(request)
            elif category.lower() == "misc":
                misc[who].append(request)
            elif category.lower() == "meat":
                meat[who].append(request)
            elif category.lower() == "sweets":
                sweets[who].append(request)
            elif category.lower() == "household":
                household[who].append(request)
            elif category.lower() == "frozen":
                frozen[who].append(request)

titles = ["Fruit and Veg", "Dairy", "Meat", "Miscellaneous", "Household", "Sweets", "Bakery", "Frozen"]
i = 0  # Initialises a variable to iterate through the titles above
for dictionary in [fruit, dairy, meat, misc, household, sweets, bread, frozen]:  # For each dictionary...
    print("\n" + titles[i].upper() + "\n")  # Print the title
    i += 1   # Add one to the i variable so it moves to the next title
    for key, value in dictionary.items():  # For each shopping owner (key) and value (list of items) in each category..
        for thing in value:  # For every item in each owner's shopping list in each category
            print(f"{thing.title()} " + "(" + f"{key.title()}" + ")"),  # Print the item in title case
