from datetime import datetime

DISC_RATE = 0.10
SALES_TAX_RATE = 0.06

subtotal = 0

print("Enter the price and quantity for each item.")

price = 1

while price != 0:
    try:
        price = float(input("Please enter the price: "))
    except ValueError:
        print("Invalid input. Please enter a valid number for price.")
        continue

    if price == 0:
        break

    while True:
        try:
            quantity = int(input("Please enter the quantity: "))
            if quantity > 0:
                break
            else:
                print("Quantity must be a positive integer. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for quantity.")

    subtotal += price * quantity

    print()
subtotal = round(subtotal, 2)
print(f"Subtotal: {subtotal:.2f}")
print()

now = datetime.now()
weekday = now.weekday()

if weekday == 1 or weekday == 2:
    if subtotal >= 50:
        discount = round(subtotal * DISC_RATE, 2)
        print(f"Discount amount: {discount:.2f}")
        subtotal -= discount
    else:
        lacking = 50 - subtotal
        print(f"To receive the discount, add {lacking:.2f} to your order.")
else:
    print(f"No discount today. Come back on Tuesday or Wednesday for 10% off!")

sales_tax = round(subtotal * SALES_TAX_RATE, 2)
print(f"Sales tax amount: {sales_tax:.2f}")

total = round(subtotal + sales_tax, 2)

print(f"Total: {total:.2f}")
