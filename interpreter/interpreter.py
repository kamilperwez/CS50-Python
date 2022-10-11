expr=input('Expression: ').split()
x=float(expr[0])
y=float(expr[2])
match expr[1]:
    case '+' : print(round(x+y,1))
    case '-' : print(round(x-y,1))
    case '*' : print(round(x*y,1))
    case '/' : print(round(x/y,1))
    case _ :print('Invalid')
