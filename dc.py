import copy
li=[[1,2],3,4]
deep=copy.deepcopy(li)
deep[0][0]=1
print(id(deep[0][0]))
print(id(li[0][0]))