year = int(input('enter your year '))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('year is leap yr')
else:
    print('not leap')
