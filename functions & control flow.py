#Qn.1
def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Parameters:
    - price (float): The original price of the item.
    - discount_percent (float): The discount percentage to be applied.

    Returns:
    - float: The final price after applying the discount or the original price if the discount is less than 20%.
    """
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price

#Qn.2
# Prompt the user for inputs
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price using the calculate_discount function
final_price = calculate_discount(original_price, discount_percentage)

# Print the result
if final_price < original_price:
    print(f"The final price after applying the discount is: {final_price:.2f}")
else:
    print(f"No discount applied. The original price is: {original_price:.2f}")
