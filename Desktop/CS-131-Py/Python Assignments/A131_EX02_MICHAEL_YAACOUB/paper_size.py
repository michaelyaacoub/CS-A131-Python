# --------------------------------------
# Name: Michael Yaacoub
# Date: 02/08/2023
# Exercise 2, part A
# --------------------------------------

# Const values
LETTER_WIDTH = 8.5
LETTER_HEIGHT = 11
MILLIMETER_PER_INCH = 25.4

# Calculate size per millimeters
paper_width_per_mm = LETTER_WIDTH * MILLIMETER_PER_INCH      # For width
paper_height_per_mm = LETTER_HEIGHT * MILLIMETER_PER_INCH    # For height

# Result output
print(f'Letter size paper is {paper_width_per_mm} mm by {paper_height_per_mm} mm.')
