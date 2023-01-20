from array import *
A = array('i', [])
size = int(input(''))
for i in range(size):
    s = int(input(''))
    A.append(s)
i = 0
for i in range(size):
    print(A[i], end=' ')
print('\n')
x = int(input(''))
A.pop(x)
i = 0
for i in range(size-1):
    print(A[i], end=' ')