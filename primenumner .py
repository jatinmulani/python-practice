n = int(input('enter a number : '))


# check whether the number is prime or not ?
# it has two factor --> 1 and self(number khud hai )
is_prime = True
for i in range(2, n):
    if (n % i == 0):
        is_prime = False
print(is_prime)
