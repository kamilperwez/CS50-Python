x=50
y=0
while x>0:
    print('Amount Due: ',x)
    y=int(input('Insert Amount: '))
    if y==5 or y==10 or y==25:
        x=x-y
        if x<0:
            print('Change Owed: ',abs(x))
        elif x==0:
            print('Change Owed: ',x)
    else:
        continue
