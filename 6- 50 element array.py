from array import *
arr = array('i', [])
size = 10
temp = 0
x = 0
for i in range(10):
    x = int(input(""))
    arr.append(x)
i = 0
while i < size:
    print(arr[i], end=" ")
    i += 1
print("\n")
i = 0
while i < size:
    temp = arr[i]
    arr[i] = arr[i+1]
    arr[i+1] = temp
    i += 2
i = 0
for i in range(size):
    print(arr[i], end=" ")
