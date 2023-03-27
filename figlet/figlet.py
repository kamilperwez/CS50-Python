from pyfiglet import Figlet
import random
import sys
figlet=Figlet()
fonts=figlet.getFonts()
if len(sys.argv)==1:
    ft=random.choice(fonts)
    figlet.setFont(font=ft)
elif len(sys.argv)==3:
    if sys.argv[1]=='-f' or sys.argv[1]=='--font':
        try:
            figlet.setFont(font=sys.argv[2])
        except:
            sys.exit(1)
    else:
        sys.exit('invalid first command')
else:
    sys.exit('Invalid command Line data')
str=input('Enter Text ')
print(figlet.renderText(str))
