#        *
#       * *
#     *   *
#   *     *
# * * * * *
for i in range(1, 6):
    for j in range(1, 5-i+1):
        print(" ", end=" ")
    for k in range(1, i+1):
        if (k == 1 or i == 5 or k == i):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("")
