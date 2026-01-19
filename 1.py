# 1. Write a Python program to find the maximum element in a list of numbers without
# max functions
# numbers = [10, 20, 4, 45, 99]
# The maximum element is: 99
number = [10, 20, 4, 45, 99]
max = number[0]
for i in number:
    print(i, max)
    if (i > max):
        max = i
print("maxium number from the above list is :: ", max)
# output=>
# 10 10
# 20 10
# 4 20
# 45 20
# 99 45
# maxium number from the above list is ::  99
