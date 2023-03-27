import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches:= re.search(r"^<iframe.*src=\"https?://(www\.)?youtube\.com/embed/(\w+)\".*></iframe>",s):
        return (f'https://youtu.be/{matches.group(2)}')
    else :
        return None

if __name__=='__main__':
    main()
