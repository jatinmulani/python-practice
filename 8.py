mylist = [123, 500, 60, 400, 30]
mini = mylist[0]
for i in mylist:
    print(i, mini)
    if (i < mini):
        mini = i
        print("minimum number ", mini)
# minimum number from ths list
