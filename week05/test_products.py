"""
Test the read_dictionary function from receipt.py
"""

from receipt import read_dictionary
import pytest


def test_read_dictionary():
    """Verify that the read_dictionary function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the read_dictionary function and store the returned
    # dictionary in a variable named products_dict.
    products_dict = read_dictionary("products.csv", 0)

    # Verify that the products_dict contains 16 items.
    assert len(products_dict) == 16

    # Verify that the products_dict contains the expected items.
    assert products_dict["D150"] == ["D150", "1 gallon milk", "2.85"]
    assert products_dict["D083"] == ["D083", "1 cup yogurt", "0.75"]
    assert products_dict["W112"] == ["W112", "wheat bread", "2.55"]


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
