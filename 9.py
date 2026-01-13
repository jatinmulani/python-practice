data = "sanarsh"
start = 0
end = len(data)-1
while (start < len(data)-1):
    if (data[start] == data[end]):
        print(start, end, data[start], data[end])
    end += 1
    if (end == start):
        end = len(data)-1
        start += 1
