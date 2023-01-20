from array import *
A = array('i', [])
x = array('d', [])
size = 100
size1 = size
temp = 0
d = 0
for i in range(size):
    s = int(input(''))
    A.append(s)
i = 0
for i in range(size):
    print(A[i], end=' ')
print('\n')
while d <= size:
    temp = A[size-1]
    x.append(temp)
    size -= 1
while d < size1:
    print(x[d], end=' ')
    d += 1