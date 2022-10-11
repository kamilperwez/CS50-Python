cc=input('camelCase: ')
sc=''
for i in range(len(cc)):
    if cc[i].isupper():
        sc=sc+('_')+(cc[i].lower())
    else:
        sc=sc+(cc[i])
print('snake_case: ',sc)
