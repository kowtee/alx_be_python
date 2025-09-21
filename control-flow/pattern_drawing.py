# pattern_drawing.py
# Draws a square pattern of asterisks (*) using a while loop and nested for loop.

size = int(input("Enter the size of the pattern: "))

row = 0
while row < size:
    # print one row of asterisks without automatic newline
    for _ in range(size):
        print("*", end="")
    print()  # move to the next line after each row
    row += 1
