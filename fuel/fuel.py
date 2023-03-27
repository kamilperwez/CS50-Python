rdef main():
    val=getVal('Fraction: ')
    if val <=0.01:
        print('E')
    elif val >=0.99:
        print('F')
    else:
        print(f'{int(round(val*100))}%')
def getVal(prompt):
    while True:
        try:
            z= input(prompt)
            x,y=z.split('/')
            x=int(x)
            y=int(y)
            f=x/y
            if x>y:
                continue
        except ValueError:
            continue
        except ZeroDivisionError:
            continue
        else:
            return f
main()









