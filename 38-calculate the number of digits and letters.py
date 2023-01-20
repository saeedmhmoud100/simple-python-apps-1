import string

text = input('Enter a text: ')
num_l=0
num_d=0

for i in text:
    if i in string.ascii_letters: num_l+=1
    if str(i).isdigit(): num_d+=1

print('Litters:',num_l)
print('Digits:',num_d)