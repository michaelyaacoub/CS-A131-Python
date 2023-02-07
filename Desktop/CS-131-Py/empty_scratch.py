# values = [6, 2, 4, 12, 39, 82, 73, 5]
# values.sort()
# print("sorted: ", values)
#
# values.append(00)
# print("appended: ", values)
# values.insert(3, "Michael")
# values.insert(4, "Korina")
# print("inserted: ", values)
# values.pop(len(values)-1)
# print("popped: ", values)
# print()
# prices = list(values)
# print("new list, prices: ", prices)
# print("values: ", values)
# print("prices: ", prices)
# prices.pop(3)
# print("popped prices: ", prices)
#
# print()
# prices.remove(90)
# length = prices[0: len(values) -1]
# print("Length: ", length)


# values = [1, 4, 2, 234, 1, 3]
# result = 0.0
# for i in values:
#     result = result + i
#
# print(result)

# def arr_func():
#     friends = ["Michael", "John", "Korina", "babe"]
#     result = ""
#     for i in range(len(friends)):
#         if i > 0:
#             result = result + " | "
#         result = result + friends[i]
#     print(result)
#
#
# if __name__ == arr_func():
#     arr_func()

# friends = ["Michael", "John", "Korina", "babe"]
#
# myfriends = ""
# for i in range(len(friends) - 1, -1, -1):
#     if i < len(friends) - 1:
#         myfriends = myfriends + ", "
#     myfriends = myfriends + friends[i]
# print(myfriends, end="")

# values = [1, 2, 34, 53, 10, 122, 35]
# longest = values[0]
# smallest = values[0]
# for i in range(1, len(values) - 1):
#     if values[i] > longest:
#         longest = values[i]
#     elif values[i] < smallest:
#         smallest = values[i]
#
# print("longest: ", longest)
# print("smallest: ", smallest)
# print()
#
# limit = 100
# pos = 0
# found = False
# while pos < len(values) and not found:
#    if values[pos] == limit:
#       found = True
#    else:
#       pos = pos + 1
#
# if found:
#    print("found")
# else:
#    print("not found")


in_file = open("book.txt", "r")
out_file = open("output.txt", "w")
number = 1
for line in in_file:
    out_file.write(str(number) + "- " + line)
    number = number + 1

in_file.close()
out_file.close()