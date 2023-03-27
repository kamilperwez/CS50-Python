import csv,sys
def main():
    if len(sys.argv) <=2:
        print('Too few command-line arguments')
        sys.exit(1)
    elif len(sys.argv)==3:
        file1=sys.argv[1]
        file2=sys.argv[2]
        try:
            if (file1.rstrip().endswith('.csv')):
                with open(file1) as fil1:
                    reader=csv.DictReader(fil1)
                    if (file2.rstrip().endswith('.csv')):
                        with open(file2,'w') as fil2:
                            fn=["first","last","house"]
                            writer=csv.DictWriter(fil2,fieldnames=fn)
                            writer.writeheader()
                            for rows in reader:
                                last,first=rows['name'].split(', ')
                                home=rows['house']
                                writer.writerow({"first":first,"last":last,"house":home})
                            sys.exit(0)
                    elif file2.endswith('.csv')==False:
                        print('Not a CSV file')
                        sys.exit(1)
            elif file1.endswith('.csv')==False:
                print('Not a CSV file')
                sys.exit(1)
        except FileNotFoundError:
            sys.exit('File not Found')
    else:
        sys.exit('Too many command-line arguments')
if __name__=="__main__":
    main()