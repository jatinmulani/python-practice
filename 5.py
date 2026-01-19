# write a program to remove duplicate from a list while maintaining the order of elements
# a. number=[1,2,2,3,3,4,4,4,5]
# b. list after removing duplicate from list :[1,2,3,4,5]
number = [1, 2, 2, 3, 3, 4, 4, 4, 5]
uniq = []
dupl = []
for i in number:
    if i not in uniq:
        uniq.append(i)
    else:
        dupl.append(i)
print('after removal of dupl list==', uniq)
print("duplicate chacracter ", dupl)
