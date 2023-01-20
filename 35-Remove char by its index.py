strg = input("Enter string: ")
n = int(input("Index u wanna remove from the string: "))
if n < len(strg):
    print(strg[:n-1]+strg[n+1:])
else:
    print("Out of range")