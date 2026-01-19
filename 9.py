# write a python to check if a list is a  palindrome (reads the same backward as forward ) using two pointer approch
# a. number =[1,2,3,2,1]
# b true

number = [1, 2, 2, 2, 1]
start = 0
a = 100
end = len(number)-1
while (start < end):
    if (number[start] != number[end]):
        a = 101
        break
    start += 1
    end -= 1
if (a == 101):
    print("  not palindrome")
else:
    print("  palindrome")
