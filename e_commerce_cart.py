# e_commerce_cart.py

def calculate_total_price(cart_items):
    """
    Calculate the total price of items in the cart.
    Applies a 10% discount if the cart has more than 5 items.
    
    Parameters:
    cart_items (dict): Dictionary containing item names and their prices.

    Returns:
    float: Final price after discount (if applicable).
    """
    if not cart_items:
        print("The cart is empty.")
        return 0.0

    total_items = len(cart_items)
    total_price = sum(cart_items.values())

    if total_items > 5:
        print("Applying 10% discount for more than 5 items.")
        total_price *= 0.9  # Apply 10% discount

    return total_price

def main():
    cart_items = {
        'Laptop': 50000,
        'Headphones': 2000,
        'Mouse': 500,
        'Keyboard': 1500
        # Add more items to test > 5 items discount
    }

    total = calculate_total_price(cart_items)
    if total > 0:
        print(f"Total Price: {total}")

if __name__ == "__main__":
    main()
