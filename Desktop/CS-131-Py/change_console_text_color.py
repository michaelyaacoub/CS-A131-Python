from random import randint
from sty import fg


# WORKS ON LINUX


def generateRGB():
    reds = randint(0, 256)
    greens = randint(0, 256)
    blues = randint(0, 256)
    return reds, greens, blues


def generateColour(reds, greens, blues):
    return fg(reds, greens, blues)


reds, greens, blues = generateRGB()
colour = generateColour(reds, greens, blues)

print(colour, "I'm randomly changing colours muahahahahahaha!!", fg.rs)
