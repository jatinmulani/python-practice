# when a loop from the value 450 in the backward direction and you neet to printthose value up to 5 digit which are divided by 9 and 7
i = 450
x = 0
while (x < 5):
    if (i % 9 == 0 and i % 7 == 0):
        print(i, x)
        x += 1
    i -= 1
