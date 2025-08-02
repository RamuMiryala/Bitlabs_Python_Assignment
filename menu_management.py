# menu_management.py

def add_menu_item(menu, item):
    """
    Adds a new item to the menu if it doesn't already exist.

    Parameters:
    menu (list): Current menu list.
    item (str): Item to be added.

    Returns:
    list: Updated menu.
    """
    if item not in menu:
        menu.append(item)
    else:
        print(f"{item} already exists in the menu.")
    return menu

def remove_menu_item(menu, item):
    """
    Removes an item from the menu if it exists.

    Parameters:
    menu (list): Current menu list.
    item (str): Item to be removed.

    Returns:
    list: Updated menu.
    """
    if item in menu:
        menu.remove(item)
    else:
        print(f"{item} not found in the menu.")
    return menu

def check_menu_item(menu, item):
    """
    Checks whether a specific item is available in the menu.

    Parameters:
    menu (list): Current menu list.
    item (str): Item to be checked.

    Returns:
    str: Availability message.
    """
    return f"{item} is available" if item in menu else f"{item} is not available"

def main():
    initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
    add_item = "Tacos"
    remove_item = "Salad"
    check_item = "Pizza"

    print("Original menu:", initial_menu)
    
    # Add and remove items
    updated_menu = add_menu_item(initial_menu, add_item)
    updated_menu = remove_menu_item(updated_menu, remove_item)

    # Display updated menu
    print("Updated menu:", updated_menu)

    # Check item availability
    availability = check_menu_item(updated_menu, check_item)
    print("Availability:", availability)

if __name__ == "__main__":
    main()
