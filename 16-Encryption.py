word = input("Enter word: ")
new_word = ""
for i in word:
    if i == 'z':
        asci = 'a'
        new_word = new_word + asci
    else:
        asci = ord(i) + 1
        new_word = new_word + chr(asci)
print(new_word)