start = int(input('Enter the start: '))
end = int(input('Enter the end: '))
nums=[]
for i in range(start,end+1):
    if not i%9 and i%4:
        nums.append((i))

print(str(nums)[1:-1])