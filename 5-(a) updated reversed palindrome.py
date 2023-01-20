word = input("")
reversed_string = ""
for i in word:
    reversed_string = i+reversed_string
print(reversed_string)
if reversed_string == word :
    print("Palindrome")