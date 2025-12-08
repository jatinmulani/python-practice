passward = input('enter from user : ')
valid_len = len(passward) >= 8
has_digit = False
has_upper = False
has_lower = False
has_speical = False
for c in passward:
    if c.isdigit():
        has_digit = True
    elif c.isupper():
        has_upper = True
    elif c.islower():
        has_lower = True
    elif not c.isalnum():
        has_speical = True
if has_digit and has_upper and has_lower and valid_len and has_speical:
    print('strong password')
else:
    print('weak password')
