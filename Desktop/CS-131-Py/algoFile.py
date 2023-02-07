"""
Practing my Files and exceptions

"""


# Practice with Files and Exceptions

def process_file(input_file, outputs):
    """reads and writes to files"""

    # open input and output files
    try:
        in_file = open(input_file, "r")
        out_file = open(outputs, "w")

        # rest of the code ...

    except Exception as e:
        print(f"Error: {e}")


    # local variables
    total = 0
    count = 0
    min_val = float('inf')
    max_val = float('-inf')

    # processing algorithm
    line = in_file.readline()
    while line != "":
        value = float(line)
        total += value
        count += 1
        out_file.write("Total: %15.2f\n" % value)

        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value

        line = in_file.readline()

    out_file.write("%24s\n" % "--------")
    out_file.write("Total: %15.2f\n" % total)

    average = total / count
    out_file.write("Average: %12.2f\n" % average)
    out_file.write("Min: %16.2f\n" % min_val)
    out_file.write("Max: %17.2f\n" % max_val)

    # close files
    in_file.close()
    out_file.close()
