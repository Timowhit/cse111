# Quick Reference Guide

## File Locations
All project files are in: `c:\Users\white\Projects\github\timowhit\cse111\week05\`

## Quick Commands

### Navigate to project folder:
```powershell
cd c:\Users\white\Projects\github\timowhit\cse111\week05
```

### Run the program:
```powershell
python receipt.py
```

### Run tests:
```powershell
python test_products.py
```

## What Each File Does

| File | Purpose |
|------|---------|
| `receipt.py` | Main program - generates receipts |
| `test_products.py` | Tests for read_dictionary function |
| `products.csv` | Product catalog (16 items) |
| `request.csv` | Customer order (sample data) |
| `README.md` | Full documentation |
| `PROJECT_SUMMARY.md` | Project overview and checklist |

## Key Functions

### `read_dictionary(filename, key_column_index)`
- Opens and reads CSV file
- Creates dictionary with specified column as key
- Returns the dictionary

### `main()`
- Reads product catalog
- Reads customer order
- Calculates totals and tax
- Displays formatted receipt
- Handles errors

## Enhancements Included

1. **New Year Sale Countdown** - Days until Jan 1
2. **Return Date** - 30 days from purchase
3. **Random Coupon** - 20% off a purchased item

## Error Types Handled

- `FileNotFoundError` - Missing CSV files
- `PermissionError` - File access denied
- `KeyError` - Invalid product ID

## Sample Data

**Products in Catalog:** 16 items (D150, D083, D215, P019, P020, P021, P025, P143, W231, W112, C013, H001, H014, H020, H021, H025)

**Sample Order:**
- wheat bread: 2
- 1 cup yogurt: 4
- 32 oz granola: 1
- twix candy bar: 2
- 1 cup yogurt: 3

**Expected Results:**
- Items: 12
- Subtotal: $15.26
- Tax (6%): $0.92
- Total: $16.18
