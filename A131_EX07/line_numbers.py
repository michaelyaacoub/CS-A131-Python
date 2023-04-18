"""
-------------------------------
Name: Michael Yaacoub
Date: Apr/15/2023
Assignemnt: EX07 - Part B
-------------------------------
Write a program that reads a file containing text. 
Read each line and send it to the output file, 
preceded by line numbers.
"""

def number_lines():
    """ Reads a file. """
    filename = input("Enter a file name: ")
    output_filename = input("Enter the output file name: ")
    with open(filename, 'r') as infile, open(output_filename, "w") as outfile:
        count_lines = 0
        for line in infile:
            if line != "":
                count_lines = count_lines + 1
            print("/* " + str(count_lines) + "*/ " + line.strip())
            outfile.write("/*" + str(count_lines) + "*/" + line)

if __name__ == "__main__":    
    number_lines()
