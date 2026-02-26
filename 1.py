#1, # Find Frequency of Each Element
# nums = [1, 2, 2, 3, 1, 4, 2]
# freq = {}
# for i in nums:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1

# print(freq)


# # 2. Rotate a List Left by One Position
# # 1st method
# a = [10, 20, 30, 40, 50]
# k=5
# for  i in range(k):
#     x=a.pop()
#     a.insert(0,x)
#     k+=1
#     print(a)

# # by vinay sir method
# # step1 reverse the  table
# # step2  revere 0 se k-1
# # reverse  k to n-1

# li=[1,2,3,4,5]
# k=2
# left=0
# right=len(li)-1
# while(left<right):
#     li[left],li[right]=li[right],li[left]
#     left+=1
#     right-=1
# left=0
# right=k-1
# while(left<right):
#     li[left],li[right]=li[right],li[left]
#     left+=1
#     right-=1
# left=k
# right=len(li)-1
# while(left<right):
#     li[left],li[right]=li[right],li[left]
#     left+=1
#     right-=1
# print(li)

# #  q3 ->Find Index of All Occurrences of a Given Element target 7
# a=[1,2,3,4,5]
# for i in range(len(a)):
#     for j in range(i+1,len(a)) :
#         if(a[i]+a[j]==7):
#             print(i,j)

# # q4 Remove All Negative Numbers from a List
# nums = [3, -1, 5, -7, 8, -2]
# new=[]
# for i in nums:
#     if(i>0):
#         new.append(i)
# print(new)

# #  q5 ->Check Whether a List is Palindrome
# s=[1,2,1,5]
# index = 0
# a = 1
# last = len(s)-1
# while (index < len(s)):
#     if (s[index] != s[last]):
#         a = 2
#         break
#     print("index", index, s[index], s[last])
#     index += 1
#     last -= 1
# if (a == 2):
#     print('not a palindrome')
# else:
#     print('palindrome')

# q=>6 # Merge Two Lists and Remove Duplicates
# list1 = [1, 2, 3]
# list2 = [3, 4, 5]
# list3=list1+list2
# uniq=[]
# dupl=[]
# for i in list3:
#     if(i not in uniq):
#         uniq.append(i)
#     else:
#         dupl.append(i)
# print(uniq)


# #  q7 => Find Missing Number from 1 to n
# nums = [1, 2, 4, 5, 6]
# n=len(nums)+1
# total_sum=n*(n+1)//2
# missing=total_sum-sum(nums)
# print(missing)

#  q8 => Remove Elements That Appear More Than Once
nums = [1, 2, 2, 3, 4, 4, 5]
uniq=[]
dupl=[]
for i in nums:
    if(i not in uniq):
        uniq.append(i)
    else:
        dupl.append(i)
print(uniq)