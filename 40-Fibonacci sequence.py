n = int(input("Size of the sequence: "))
i = 1
lst = [0, 0]
while i <= n:
    if lst[i] == 0:
        x = i + lst[i - 1]
    else:
        x = lst[i] + lst[i-1]
    lst.append(x)
    i += 1
lst.pop(0)
lst.pop(0)
print(lst)