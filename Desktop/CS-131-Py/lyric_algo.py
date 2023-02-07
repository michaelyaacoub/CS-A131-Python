"""Func that reads word per line"""
inline = open("lyrics", "r")
outline = open("words", "w")
for line in inline:
    line = line.lstrip()
    word_list = line.split()

    for word in word_list:
        word = word.rstrip(".,?!")
        print(word)
        outline.write(word)
    while line != "":
        line = inline.read(1)
        print(line)

inline.close()
outline.close()
