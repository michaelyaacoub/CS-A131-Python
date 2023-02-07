def cube(side_length) :
    """This returns whatever the prof wants"""
    volume = side_length ** 3
    return volume
# expected result bfb
result1 = cube(2)
result2 = cube(10)

# test it babe
assert cube(2) == 8
assert cube(10) == 1000
cube(12)
