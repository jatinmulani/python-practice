#  * * * * *
#   *     *
#    *   *
#     * *
#      *
l = 5
for i in range(1, 6):
    for j in range(1, i+1):
        print(" ", end="")
    for k in range(1, 6-i+1):
        if (k == 1 or i == 1 or l == k):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    l -= 1
    print("")
