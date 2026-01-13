
n = int(input('enter from user : '))
i = 1
sum = 0
while (i < n):
    if (n % i == 0):
        print(i)
        sum = sum+i
    i = i+1
print(sum)
if (n == sum):
    print('perfect number')
else:
    print('not a perfect number')
