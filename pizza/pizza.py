from tabulate import tabulate
import sys
import csv
if len(sys.argv) <=1:
    print('Too few command-line arguments')
    sys.exit(1)
elif len(sys.argv)==2:
     try:
        file=sys.argv[1]
        if (file.rstrip().endswith('.csv')):
            with open(file) as fil:
                reader=csv.DictReader(fil)
                print(tabulate(reader,headers='keys',tablefmt='grid'))
        elif file.endswith('.csv')==False:
            print('Not a CSV file')
            sys.exit(1)
     except FileNotFoundError:
        sys.exit('File not Found')
else:
     sys.exit('Too many command-line arguments')
