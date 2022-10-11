grt=input('Greeting: ')
grtl=grt.lower().strip()
if(grtl.startswith('hello')):
    print('$0')
elif(grtl.startswith('h')):
    print('$20')
else:
    print('$100')