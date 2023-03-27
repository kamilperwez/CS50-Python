lname=[]
while True:
    try:
        txt=input()
        lname.append(txt)
    except EOFError:
        break
print('Adieu, adieu, to ',end='')
for i in range(len(lname)):
    if len(lname)>=2:
        print(lname[i],end='')
        if i ==len(lname)-2:
            if i==0:
                print(' and ',end='')
            else:
                print(', and ',end='')
        elif i!=len(lname)-1:
            print(', ',end='')
    else:
        print(lname[i])
