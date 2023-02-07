

# Computes the Minimum
smallest = float(input("Enter a value: "))
inputStr = input("Enter a value: ")
while inputStr != "":
    value = float(inputStr)
    if value < smallest:
        smallest = value
    inputStr = input("Enter a value: ")


# Computes the Largest.
largest = float(input("Enter a value: "))
inputStr = input("Enter a value: ")
while inputStr != "":
    value = float(inputStr)
    if value > largest:
        largest = value
    inputStr = input("Enter a value: ")


# Define list daysInMonth assuming that the year is not a leap year.
daysInMonth = [31, 28, 31, 30, 30, 31, 31, 31, 30, 31, 30, 31]

# Read the month and year from the user
month = int(input("Month (1 - 12): "))
year = int(input("Year: "))

# Determine if it's a leap year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    """It's a leap year, adjust the entry for February"""
    daysInMonth[1] = 29

# Get the number of days in the given month
days = daysInMonth[month - 1]

# Print the number of days.
print("Number of days:", days)


### Files and Exceptions ###
# to open a file for reading only:
infile = open("input.txt", "r")

# to open a file for writing:

outfile = open("output.txt", "w")

# to close a file:
infile.close()
outfile.close()


# to obtain texts from a file: use readline() method:
infile.readline()

# print function can also be used to write to files:
outfile.write("Number of entries: %d\nTotal: %8.2f\n" % (count, total))
# OR
print("Hello, World!", file=outfile)




"""
Write a program that reads a file one
character at a time and prints out how many
times each of the vowels a e i o u occur 
(in upper- or lowercase).
Complete the following code.
"""

vowels = "aeiou"
counters = [0, 0, 0, 0, 0]

filename = input("Input file: ")

# Open the file in read mode
with open(filename, "r") as file:
    # Read the file line by line
    for line in file:
        # Iterate over each character in the line
        for char in line:
            # Convert the character to lowercase
            char = char.lower()
            
            # Check if the character is a vowel and update the corresponding counter
            if char in vowels:
                index = vowels.index(char)
                counters[index] += 1

# Print the results
for i in range(len(vowels)):
    print("%s: %d" % (vowels[i], counters[i]))

