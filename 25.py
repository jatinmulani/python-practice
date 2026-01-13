# *
# * *
# *   *
# *     *
# * * * * *
for i in range(1, 6):
    for k in range(1, i+1):
        if (k == 1 or i == 5 or i == k):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("")
