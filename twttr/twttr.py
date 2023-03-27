txt=input('Input: ')
listvow=['a','e','i','o','u','A','E','I','O','U']
for i in range(len(listvow)):
    txt=txt.replace(listvow[i],'')
print(txt)