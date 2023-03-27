import sys
ct=0
if len(sys.argv) <=1:
    print('Too few command-line arguments')
    sys.exit(1)
elif len(sys.argv)==2:
    try:
        file=sys.argv[1]
        if file.endswith('.py'):
            fil=open(file)
            for line in fil:
                line=line.strip()
                if line.startswith('#'):
                    continue
                elif len(line)>=1:
                    ct+=1
            print(ct)
        elif file.endswith('.py')==False:
            print('Not a python file')

    except:
         print('File not Found')
         sys.exit(1)
else:
    print('Too many command-line arguments')
    sys.exit(1)