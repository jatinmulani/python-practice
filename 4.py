# write a python program to sort a list in asceding order without sort function
a = [100, 20, 5, 40, 8, 10]
n = len(a)
for i in range(n-1):
    for j in range(n-1-i):
        if (a[j] > a[j+1]):
            a[j], a[j+1] = a[j+1], a[j]
print(a)
