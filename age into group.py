age = int(input('enter your age'))
if (age <= 1):
    print("infant")
elif (age >= 2 and age <= 4):
    print("toddler")
elif (age >= 5 and age <= 12):
    print("child")
elif (age >= 13 and age <= 19):
    print("tennager")
elif (age >= 20 and age <= 59):
    print("adult")
else:
    print("senior citizen")
