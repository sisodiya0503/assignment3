import math
number = float(input("Enter a number: "))
if number >= 0:
    square_root = math.sqrt(number)
else:
    square_root ="not define for negative numbers"

if number >= 0:
    natural_log = math.log(number)
else:
    natural_log = "not define for negative numbers"

sine_value = math.sin(number)

print(f"\nResults for the number {number}:")
print(f"Square root: {square_root}")
print(f"Natural logarithm (ln): {natural_log}")
print(f"Sine (in radians): {sine_value}")