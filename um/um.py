import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    umlist=re.findall(r'(\b|\W)um(\b|\W)',s,re.IGNORECASE)
    print(umlist)
    return len(umlist)




if __name__ == "__main__":
    main()