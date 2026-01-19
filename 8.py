# write a python  program to find the sum of the elements in a list , excluding the largest and smallest element. dont use max or min function
# a. number=[1,2,3,4,5]
# b. sum excluding the largest and smallest element:9
number = [1, 2, 3, 4, 5]
badanumber = number[0]
chotanumber = number[0]
total = 0
for i in number:
    if (i < chotanumber):
        chotanumber = i

    if (i > badanumber):
        badanumber = i

for i in number:
    if (i != chotanumber and i != badanumber):
        total += i
print(total)
