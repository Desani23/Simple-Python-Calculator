def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage to apply.

    Returns:
    float: The final price after applying the discount, or the original price if the discount is less than 20%.
    """
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    else:
        return price

# Prompting user input
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculating and printing the final price
final_price = calculate_discount(price, discount_percent)
print(f"Final price: {final_price:.2f}")

