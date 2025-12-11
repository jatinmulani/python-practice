n = 6
fact_count = 0
for i in range(1, n+1):
    if (n % i == 0):
        fact_count += 1
if (fact_count > 2):
    print('not a prime number')
else:
    print('prime number ')
