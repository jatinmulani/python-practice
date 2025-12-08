a = input('enter from user: ')
prime_digits = {'2', '3', '5', '7'}
count = 0
for ch in a:
    if not ch.isdigit():
        print(ch)
        continue
    if ch in prime_digits:
        count += 1
print('prime_digits count:', count)
