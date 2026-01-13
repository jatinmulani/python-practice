# 12345
# 3456
# 567
# 78
# 9
# x = 1
# for i in range(6, 0, -1):
#     for j in range(1, i):
#         print(j+x-1, end="")
#     print()
#     x += 2
# num = 1
# rows = 5

# for i in range(rows):
#     for j in range(rows - i):
#         print(num, end="")
#         num += 1
#     print()
start = 1

for i in range(1, 6):
    num = start
    for j in range(1, 6 - i + 1):
        print(num, end="")
        num += 1
    start += 2
    print()
