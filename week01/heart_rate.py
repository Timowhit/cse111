"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
maximum_heart_rate = 220 - int(input("Enter your age: "))
lower_bound = int(maximum_heart_rate * 0.65)
upper_bound = int(maximum_heart_rate * 0.85)
print(f"When exercising to strengthen your heart,")
print(f"keep your heart rate between {lower_bound} and {upper_bound} beats per minute.")