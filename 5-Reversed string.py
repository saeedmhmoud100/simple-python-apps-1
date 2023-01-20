word = input("")
re = reversed(word)
print("".join(re))


or



word = input("")
print(word[-1: :-1])


or



word = input("")
reversed_string = ""
for i in word:
    reversed_string = i+reversed_string
print(reversed_string)
