# --------------------------------------
# Name: Michael Yaacoub
# Date: 02/08/2023
# Exercise 2, part B
# --------------------------------------

# Importing the math library to get sqrt
from math import sqrt

# Const values
LETTER_WIDTH = 8.5
LETTER_HEIGHT = 11

# Calculate size in perimeter and diagonal
in_perimeter = 2 * (LETTER_WIDTH + LETTER_HEIGHT)               # In perimeter
in_diagonal = sqrt(LETTER_WIDTH ** 2 + LETTER_HEIGHT ** 2) # In doiagonal

# Result output
print(f'The perimeter is {in_perimeter} inches.')
print(f'The length of the diagonal is {in_diagonal} inches.')
