# 4567
# 567
# 56
# 5
# x = 4

# for i in range(1, 5):

#     for j in range(1, 5-i+1):
#         print(x+j-1, end="")
#     x += 1
#     print("")


# using third varaible
x = 4
for i in range(1, 5):
    temp = x
    for j in range(1, 5-i+1):
        print(temp, end="")
        temp += 1
    x += 1
    print("")
