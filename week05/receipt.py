# Enhancement: This program includes three enhancements to exceed requirements:
# 1. Calculates and displays days until New Year's Sale (Jan 1)
# 2. Displays a "return by" date (30 days from purchase at 9:00 PM)
# 3. Prints a random coupon for one of the purchased products

import csv
from datetime import datetime, timedelta
import random


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(row_list) != 0:
                # From the current row, retrieve the data
                # from the column that contains the key.
                key = row_list[key_column_index]

                # Store the data from the current
                # row into the dictionary.
                dictionary[key] = row_list

    # Return the dictionary.
    return dictionary


def main():
    try:
        # Call the read_dictionary function and store the products dictionary
        # in a variable named products_dict.
        products_dict = read_dictionary("products.csv", 0)

        # Print the store name at the top of the receipt.
        print("Inkom Emporium")

        # Initialize variables for totals
        num_items = 0
        subtotal = 0.0
        
        # List to store product names for coupon generation
        purchased_products = []

        # Open the request.csv file for reading.
        with open("request.csv", "rt") as request_file:
            # Use the csv module to create a reader object
            # that will read from the opened CSV file.
            reader = csv.reader(request_file)

            # Skip the first line of the request.csv file because
            # the first line contains column headings.
            next(reader)

            # Read each row from the request.csv file one row at a time.
            for row_list in reader:
                # Get the product number and quantity from the current row.
                product_number = row_list[0]
                quantity = int(row_list[1])

                # Use the product number to find the corresponding item
                # in the products_dict.
                product_info = products_dict[product_number]

                # Get the product name and price from the product_info list.
                product_name = product_info[1]
                product_price = float(product_info[2])

                # Print the product name, quantity, and price.
                print(f"{product_name}: {quantity} @ {product_price}")
                
                # Add to purchased products list (avoid duplicates)
                if product_name not in purchased_products:
                    purchased_products.append(product_name)

                # Update the number of items and subtotal
                num_items += quantity
                subtotal += quantity * product_price

        # Calculate sales tax (6%)
        sales_tax = subtotal * 0.06
        
        # Calculate total
        total = subtotal + sales_tax

        # Print the totals
        print()
        print(f"Number of Items: {num_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")
        print()
        
        # Print thank you message
        print("Thank you for shopping at the Inkom Emporium.")
        
        # Get and print current date and time
        current_date_time = datetime.now()
        print(current_date_time.strftime("%a %b %d %H:%M:%S %Y"))
        
        # Enhancement 1: Calculate days until New Year's Sale
        current_year = current_date_time.year
        new_year = datetime(current_year + 1, 1, 1)
        days_until_sale = (new_year - current_date_time).days
        print(f"\nNew Year's Sale starts in {days_until_sale} days!")
        
        # Enhancement 2: Calculate and print return by date (30 days at 9:00 PM)
        return_by_date = current_date_time + timedelta(days=30)
        return_by_date = return_by_date.replace(hour=21, minute=0, second=0, microsecond=0)
        print(f"Return by: {return_by_date.strftime('%a %b %d %I:%M %p %Y')}")
        
        # Enhancement 3: Print a random coupon for one of the purchased products
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


# If this file is executed like this:
# > python receipt.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
