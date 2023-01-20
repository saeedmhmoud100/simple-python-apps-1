n = int(input("n: "))
s = 1
for i in range(1, n-1, 4):
    x = 1/(i+2)
    y = 1/(i+4)
    s = s - x + y
    print(x, y)
print(s*4)
