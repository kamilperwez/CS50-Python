def main():
    grt=input('Greeting: ')
    print(f'${value(grt)}')
def value(greeting):
    grtl=greeting.lower().strip()
    if(grtl.startswith('hello')):
         return 0
    elif(grtl.startswith('h')):
        return 20
    else:
        return 100
if __name__ == "__main__":
    main()
