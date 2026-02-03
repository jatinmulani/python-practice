# 1st
# my_list = [10, 20, 30, 40, 50]
# # print(my_list[2])
# list_lenth=len(my_list)
# if(list_lenth==0):
#     print("list is empty")
# else:
#     print("list is not empty")
# # 2nd
# my_list = [10, 20, 30, 40, 50]
# # Change Element: Change the second element of a list to 200 and print the updated list
# my_list[1]=200
# # Append Element: Add 600 o the end of a list and print the new list.

# my_list.append(600)
# # Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
# my_list.insert(2,300)
# # Remove Element (by value): Remove 600 from the list and print the list.
# my_list.remove(600)
# # Remove Element (by index): Remove the element at index 0 from the list print the list.
# my_list.pop(0)
# print(my_list)

# # 3rd
# my_list = [10, 20, 30, 40, 50]
# sum=0
# avg=0

# for i in my_list:
#     sum=sum+i
    
# print(sum)
# avg=sum//len(my_list)
# print(avg)

# 4th reverse a list
# list1 = [100, 200, 300, 400, 500]
# list1.sort(reverse=True)
# print(list1)

# # 5th turn into sqare
# numbers = [1, 2, 3, 4, 5, 6, 7]
# for i in numbers:
#     print(i*i)

# 6th find maximum and minimum
data = [8, 2, 15, 1, 9]
max=data[0]
second_largest=data[0]
third_largetst=data[0]
for i in data:
   if(i>max):
      max=second_largest
      max=i
    
   elif(i>second_largest and i!=max):
      second_largest=third_largetst
      second_largest=i
   elif(i>third_largetst and i!=second_largest):
      third_largetst=i
print(third_largetst)
print(second_largest)

# # 7th question count occurencce
# sports = ['Cricket', 'Football', 'Hockey', 'Football', 'Tennis']
# count=0
# for i in sports:
#     if(i=='Football'):
#         count+=1
# print(count)

# # 8th sort a list of  number
# numbers = [5, 2, 8, 1, 9]
# numbers.sort()
# print(numbers)

# # 9th
# a=[10,20,30]
# b=a[:]
# print("b",b)
# print("a",a)

# # 10th combine 2 list
# list_a = [1, 2]
# list_b = [3, 4]
# c=list_a+list_b
# print(c)

# 11th remove empty string from the list
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# # list1.remove("")
# # list1.remove("")
# # print(list1)
# for i in list1:
#     if(i==""):
#         list1.remove("")
# print(list1)

# 12th  remove duplicate from ths list
# list_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4]
# dupl=[]
# uniq=[]
# for i in list_with_duplicates:
#     if(i not in uniq):
#         uniq.append(i)
#     else:
#         dupl.append(i)
# print(uniq)
    
# # 13th remove all occurencwe of a specific item 
# list1 = [5, 20, 15, 20, 25, 50, 20]
# for i in list1:
#     if(i==20):
#         list1.remove(20)
# print(list1)

# # 14th  list compherince 
# my_list = [1, 2, 3, 'Jessa', 4, 5, 'Kelly', 'Jhon', 6]
# list1=[]
# for i in my_list:
#     if type(i)==int:
#         list1.append(i)
# print(list1)
    
# 15th print the element '55'
# nested_list = [[10, 20, 30], [44, 55, 66], [77, 87, 99]]

# for i in nested_list:
#     for j in i:
#         if(j==55):
#             print(j)
# # 2nd method 
# nested_list = [[10, 20, 30], [44, 55, 66], [77, 87, 99]]
# print(nested_list[1][1])

# # 16th flatten nested lsit
# list_of_lists = [[1, 2], [3, 4], [5, 6, 7]]
# newlist=[]
# for i in list_of_lists:
#     for j in i:
#         # print(j)
#       newlist.append(j)
# print(newlist)

# # 17 :Write a program to add two lists index-wise.
# #  Create a new list that contains the 0th index item from both the list, 
# # then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# list3=[]
# for i in range(len(list1)):
#     list3.append(list1[i]+list2[i])
# print(list3)

#18th : Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"] 
# list3=[]
# for i in range(len(list1)): 
#     for j in range(len(list2)):
#       list3.append(list1[i]+list2[j])
    
# print(list3)

# # 19th 
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# for a,b in zip(list1,list2[::-1]):
#     print(a,b)

# # 21th Write a program to add item 7000 after 6000 in the following Python List
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)
# #  output =>>[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

# # 22th  add a list into this 
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub_list=["h","i","j"]
# list1[2][1][2].extend(sub_list)
# print(list1)

# # 23th You have given a Python list.
# #  Write a program to find value 20 in the list,
# #  and if it is present, replace it with 200. 
# # Only update the first occurrence of an item.
# list1 = [5, 10, 15, 20, 25, 50, 20]
# for i in range(len(list1)):
#     if(list1[i]==20):
#         list1[i]=200
#         break
# print(list1)

# # flatten a list
# a=[1,[2,3],4,[5,6,7]]
# b=[]
# for i in a:
#     if(type(i)==list):
#         for j in i:
#             b.append(j)

#     else:
#         b.append(i)
# print(b)

#    what is data model logical model conceptual model and physical model
# defination of super kry
# candidade key
# composite key
# b/w ,in,and ,like operator 
#   