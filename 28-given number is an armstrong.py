n = input('Enter a Number: ')
armstrong=0
for i in n:
    armstrong+=int(i)**len(n)
print('the number is armstrong: {}'.format(armstrong==int(n)))
