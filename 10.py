
total = 0
temp = n
while (n != 0):
    x = n % 10
    total += x**3

    n = n//10
    print("temp", temp, total)
