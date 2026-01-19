# find the longest word in list
# a. words=["apple","banana","strawberry","kiwi"]
#  output => strawberry
words = ["apple", "banana", "strawberry", "kiwi"]
bada = words[0]
for w in words:
    if (len(w) > len(bada)):
        bada = w
print(bada)
