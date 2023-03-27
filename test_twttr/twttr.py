def main():
    txt=input('Input: ')
    print(shorten(txt))


def shorten(wrd):
    listvow=['a','e','i','o','u','A','E','I','O','U']
    for i in range(len(listvow)):
        wrd=wrd.replace(listvow[i],'')
    return wrd


if __name__ == "__main__":
    main()
