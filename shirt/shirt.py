from PIL import Image,ImageOps
import sys
def main():
    if len(sys.argv) <=2:
        print('Too few command-line arguments')
        sys.exit(1)
    elif len(sys.argv)==3:
        file1=sys.argv[1].lower()
        file2=sys.argv[2].lower()
        #file1 as input,file2 as output
        fmt=['jpg','jpeg','png']
        if '.' in file1 and '.' in file2:
            try:
                f1=file1.split('.')[1]
                f2=file2.split('.')[1]
                if (f1 not in fmt ) or (f2 not in fmt):
                    sys.exit('Invalid Format')
                elif f1 != f2:
                    sys.exit('Format Mismatch')
                else:
                    edit_Photo(file1,file2)
            except FileNotFoundError:
                sys.exit('File not Found')
        else:
            sys.exit('Not a File Type')
    else:
        sys.exit('Too Many command-Line arguments')
def edit_Photo(input,output):
    shirt = Image.open("shirt.png")
    with Image.open(input) as im1:
        cropped =ImageOps.fit(im1, size=shirt.size)
        cropped.save('new.jpg') #to check cropped
        cropped.paste(shirt,mask=shirt)
        cropped.save(output)


if __name__=="__main__":
    main()
