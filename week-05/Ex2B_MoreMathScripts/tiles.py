length = float(input("Enter the room length in feet: "))
width = float(input("Enter the room width in feet: "))

area = length * width

tiles = area * 1.1

boxes = round(tiles/12)

print(f'Given a room area of {area:.2f} square feet, we would need {tiles:.2f} tiles which includes the \
10% coverage, and {boxes} boxes total.')