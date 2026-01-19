# write a function to remove duplicate elements from a list.
# a. numbers=[1,2,3,2,4,5,1,6]
# b,[1,2,3,4,5,6]
number = [1, 2, 3, 2, 4, 5, 1, 6, 1]
uniq = []
dupl = []
for i in number:
    if i not in uniq:
        uniq.append(i)
    else:
        dupl.append(i)
print(uniq)
