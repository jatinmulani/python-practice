mylist = [10, 20, 30, 410, 12, 12]
uniq = []
dupl = []
for i in mylist:
    if (i not in uniq):
        uniq.append(i)
    else:
        dupl.append(i)
print(dupl)
# duplicate nikalna
