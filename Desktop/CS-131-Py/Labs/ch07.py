in_file = open("book.txt", "r")
out_file = open("output.txt", "w")
number = 1
for line in in_file:
    out_file.write(str(number) + "- " + line)
    number = number + 1

in_file.close()
out_file.close()