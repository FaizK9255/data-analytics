# Using import math for square root function, then applying it to the distance formula

import math

x1 = float(input("Enter x1 coordinate: "))
y1 = float(input("Enter y1 coordinate: "))
x2 = float(input("Enter x2 coordinate: "))
y2 = float(input("Enter y2 coordinate: "))

distance = math.sqrt ((x2 - x1)**2 + (y2-y1)**2)

print(f'The distance between coordinates ({x1}, {y1}) and ({x2}, {y2}) is {distance:.2f} units.')