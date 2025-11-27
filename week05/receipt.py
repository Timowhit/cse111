# Enhancement: This program includes three enhancements to exceed requirements:
# 1. Calculates and displays days until New Year's Sale (Jan 1)
# 2. Displays a "return by" date (30 days from purchase at 9:00 PM)
# 3. Prints a random coupon for one of the purchased products

import csv
from datetime import datetime, timedelta
import random


def read_dictionary(filename, key_column_index):
    dictionary = {}

    with open(filename, "rt") as csv_file:

        reader = csv.reader(csv_file)

        next(reader)

        for row_list in reader:

            if len(row_list) != 0:
                key = row_list[key_column_index]

                dictionary[key] = row_list

    return dictionary


def main():
    try:
        products_dict = read_dictionary("products.csv", 0)

        print("Inkom Emporium")

        num_items = 0
        subtotal = 0.0
        
        purchased_products = []

        with open("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)

            next(reader)

            for row_list in reader:
                product_number = row_list[0]
                quantity = int(row_list[1])

                product_info = products_dict[product_number]

                product_name = product_info[1]
                product_price = float(product_info[2])

                print(f"{product_name}: {quantity} @ {product_price}")
                
                if product_name not in purchased_products:
                    purchased_products.append(product_name)

                num_items += quantity
                subtotal += quantity * product_price

        sales_tax = subtotal * 0.06
        
        total = subtotal + sales_tax

        print()
        print(f"Number of Items: {num_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")
        print()
        
        print("Thank you for shopping at the Inkom Emporium.")
        
        current_date_time = datetime.now()
        print(current_date_time.strftime("%a %b %d %H:%M:%S %Y"))
        
        current_year = current_date_time.year
        new_year = datetime(current_year + 1, 1, 1)
        days_until_sale = (new_year - current_date_time).days
        print(f"\nNew Year's Sale starts in {days_until_sale} days!")
        
        return_by_date = current_date_time + timedelta(days=30)
        return_by_date = return_by_date.replace(hour=21, minute=0, second=0, microsecond=0)
        print(f"Return by: {return_by_date.strftime('%a %b %d %I:%M %p %Y')}")
        
        if purchased_products:
            coupon_product = random.choice(purchased_products)
            print(f"\n*** COUPON: Save 20% on your next purchase of {coupon_product}! ***")

    except FileNotFoundError as err:
        print(f"Error: missing file")
        print(err)
    except PermissionError as err:
        print(f"Error: permission denied")
        print(err)
    except KeyError as err:
        print(f"Error: unknown product ID in the request.csv file")
        print(err)


if __name__ == "__main__":
    main()
