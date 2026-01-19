# write a python program to find all pairs of numbers in a list that add up to a specifc target sum.
# a. number=[1,2,3,4,5,6] target_sum=6
# b. pairs that add up to 6: [(3,3 ),(2,4),(1,5)]
number = [1, 2, 3, 4, 5, 6]
target_sum = 6
pairs = []
n = len(number)
for i in range(n):
    for j in range(i, n):
        if (number[i]+number[j]) == target_sum:
            pairs.append((number[i], number[j]))
print("pairs that add up to 6:", pairs)

# output=>pairs that add up to 6: [(1, 5), (2, 4), (3, 3)]
