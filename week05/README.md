# Week 05 Project: Grocery Store Receipt

This program reads CSV files containing product information and customer orders, then generates a formatted receipt.

## Files Included

- `receipt.py` - Main program file
- `test_products.py` - Test file to verify the read_dictionary function
- `products.csv` - Product catalog with product numbers, names, and prices
- `request.csv` - Customer order with product numbers and quantities

## Requirements

- Python 3.6 or higher
- pytest (for running tests)

## Setup

1. Ensure Python is installed on your system
2. Install pytest if you haven't already:
   ```
   pip install pytest
   ```

## Running the Program

### Run the main program:
```
python receipt.py
```

### Run the tests:
```
python test_products.py
```

## Program Features

The program performs the following tasks:

1. Reads product inventory from `products.csv`
2. Reads customer order from `request.csv`
3. Displays a formatted receipt with:
   - Store name
   - List of ordered items with quantities and prices
   - Number of items
   - Subtotal
   - Sales tax (6%)
   - Total amount due
   - Thank you message
   - Current date and time

## Enhancements (Exceeding Requirements)

This program includes three enhancements:

1. **Days Until New Year's Sale**: Calculates and displays how many days remain until the New Year's Sale begins (January 1)

2. **Return By Date**: Displays a "return by" date that is 30 days from the purchase date at 9:00 PM

3. **Random Coupon**: Generates a coupon for 20% off one of the products the customer purchased

## Error Handling

The program handles the following errors:

- **FileNotFoundError**: If products.csv or request.csv is missing
- **PermissionError**: If the program doesn't have permission to read the files
- **KeyError**: If a product ID in the request doesn't exist in the products catalog

## Testing Error Handling

### Test KeyError:
Add this line to the end of `request.csv`:
```
R002,5
```
Then run the program to see the KeyError handling.

### Test FileNotFoundError:
Temporarily rename `products.csv` to something else and run the program.

## Sample Output

```
Inkom Emporium
wheat bread: 2 @ 2.55
1 cup yogurt: 4 @ 0.75
32 oz granola: 1 @ 3.21
twix candy bar: 2 @ 0.85
1 cup yogurt: 3 @ 0.75

Number of Items: 12
Subtotal: 15.26
Sales Tax: 0.92
Total: 16.18

Thank you for shopping at the Inkom Emporium.
Thu Nov 27 14:30:45 2025

New Year's Sale starts in 35 days!
Return by: Fri Dec 27 09:00 PM 2025

*** COUPON: Save 20% on your next purchase of wheat bread! ***
```

## Project Structure

```
week05/
├── receipt.py           # Main program
├── test_products.py     # Test file
├── products.csv         # Product catalog
├── request.csv          # Customer order
└── README.md           # This file
```
