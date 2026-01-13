# n = int(input('enter from user : '))
# count = 0
# sum = 0
# while (n > 0):
#     count += 1
#     n = n//10
#     sum = sum+count
# print(sum)
n = int(input('enter from user : '))
sum_digits = 0

while n > 0:
    sum_digits += n % 10
    n = n // 10

print(sum_digits)
