import math

item_count = int(input("Enter the number of items: "))
box_capacity = int(input("Enter the box capacity: "))
print(f"For {item_count} items, you will need {math.ceil((item_count / box_capacity))} boxes.")
