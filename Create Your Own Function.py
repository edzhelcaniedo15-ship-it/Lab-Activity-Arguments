def order_drink(drink, size="medium", iced=False):
    """
    Returns a formatted string describing a drink order.
    """
    # Create the 'iced_text' string based on the boolean 'iced' argument
    iced_text = "iced " if iced else "hot "

    # Build the order string
    order_string = f"Your order: {size} {iced_text}{drink}"
    return order_string.title() # Use .title() for nice capitalization

print("\n--- Part 4 Output ---")

# Task 1: Order a default drink ("coffee"). Uses default size ("medium") and iced=False (hot).
print(order_drink("coffee"))

# Task 2: Order a large hot chocolate. Overrides size, keeps iced=False (hot).
print(order_drink("chocolate", "large"))

# Task 3: Order a small iced milk tea. Overrides size and iced.
# Note: iced=True can be passed positionally or as a keyword argument.
print(order_drink("milk tea", "small", iced=True))