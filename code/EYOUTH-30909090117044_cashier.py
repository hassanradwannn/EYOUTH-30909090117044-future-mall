# Future Mall Cashier
# Project ID: EYOUTH-30909090117044
# This program uses two parallel lists: product_names and product_prices.

product_names = ["T-shirt", "Shoes", "Bag", "Cap", "Watch"]
product_prices = [150, 300, 250, 100, 450]

# Bonus function: it calculates the total from the selected prices.
def calculate_total(selected_prices):
    total = 0
    for price in selected_prices:
        total = total + price
    return total


selected_prices = []
purchased_products = []

print("Welcome to Future Mall")

while True:
    print("\nProducts")
    for index in range(len(product_names)):
        print(index + 1, product_names[index], "AED", product_prices[index])
    print("0 Finish shopping")

    choice = int(input("Enter a product number: "))

    # Sentinel value 0 ends the shopping loop.
    if choice == 0:
        break

    if choice >= 1 and choice <= len(product_names):
        selected_prices.append(product_prices[choice - 1])
        purchased_products.append(product_names[choice - 1])
        print(product_names[choice - 1], "was added to your cart.")
    else:
        print("Please choose a number from the list.")

# Use the bonus function after the customer finishes shopping.
total = calculate_total(selected_prices)

# A discount is applied only when the total is more than AED 500.
discount = 0
if total > 500:
    discount = total * 0.10

final_total = total - discount

print("\n----- FUTURE MALL RECEIPT -----")
print("Products bought:")
for product in purchased_products:
    print("-", product)
print("Subtotal: AED", total)
print("Discount: AED", discount)
print("Total to pay: AED", final_total)
print("Thank you for shopping at Future Mall!")
