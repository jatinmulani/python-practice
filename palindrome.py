# left to right == right to left
s = input('enter from user : ')
index = 0
a = 1
last = len(s)-1
while (index < len(s)):
    if (s[index] != s[last]):
        a = 2
        break

    print("index", index, s[index], s[last])
    index += 1
    last -= 1
if (a == 2):
    print('not a palindrome')
else:
    print('palindrome')
