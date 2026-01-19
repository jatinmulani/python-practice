# 3. Write a Python program to reverse a list without reverse or slicing operator
# a. numbers = [1, 2, 3, 4, 5]
# b. Reversed list: [5, 4, 3, 2, 1]
number = [1, 2, 3, 4, 5]
orignal = number[:]
start = 0
end = len(number)-1
while (start < end):

    number[start], number[end] = number[end], number[start]
    start += 1
    end -= 1
print("orignal number", orignal)
print("reversed list", number)
