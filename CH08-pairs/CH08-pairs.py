"""
Names: Michael Yaacoub, Nalan Pandian, Taylen Vo
Date: Apr/18/23
Assignment: Ch. 08: LAB 2 Pairs
"""

import os

print(os.getcwd())


def common_words(file1, file2):
    with open(file1, 'r') as f1:
        words1 = set(f1.read().split())
    with open(file2, 'r') as f2:
        words2 = set(f2.read().split())
    common = words1 & words2
    return common

def write_common(file1, file2):
    common = common_words(file1, file2)
    new_file_name = file1.split('.')[0] + '-' + file2.split('.')[0] + '.txt'
    with open(new_file_name, 'w') as f:
        f.write(','.join(common))

write_common('lava.txt', 'water.txt')

