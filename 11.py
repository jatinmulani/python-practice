# find comman element in  two list
# list1=[1,2,3,4,5]
# list2=[3,4,5,6,7]
# result=[3,4,5]
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
result = []
for i in list1:
    for j in list2:
        if (i == j):
            result.append(i)
            break
print("result is ", result)
