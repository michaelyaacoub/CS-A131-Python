with open("touch.txt", "w") as infile:
    infile.write("CS is great and fun\nCS is awesome\nCS is cool\nCS is great\n")

def read_whole_thing(file):
    file.seek(0)
    contents = file.read()
    print(contents)

def read_by_line(file):
    file.seek(0)
    for line in file:
        print(line.rstrip())

def read_by_word(file):
    file.seek(0)
    for line in file:
        words = line.split()
        for word in words:
            print(word)

def read_by_character(file):
    file.seek(0)
    while True:
        char = file.read(1)
        if not char:
            break
        print(char)

if __name__ == '__main__':
    with open("touch.txt", "r") as infile:
        read_whole_thing(infile)
        read_by_line(infile)
        read_by_word(infile)
        read_by_character(infile)
