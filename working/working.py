import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    format=re.search(r"^([0-9][0-2]?):?([0-5][0-9])? (A|P)M to ([0-9][0-2]?):?([0-5][0-9])? (P|A)M$",s)
    if format:
        pieces=format.groups()
        hr1,hr2=pieces[0],pieces[3]
        min1,min2=pieces[1],pieces[4]
        if min1==None:
            min1='00'
        if min2==None:
            min2='00'
        if int(pieces[0]) >12 or int(pieces[3]) >12:
            raise ValueError
        else:
            if 'A' in pieces[2] and 'P' in pieces[5]:
                if pieces[0]=='12':
                    hr1='0'
                if pieces[3]=='12':
                    hr2='12'
                else:
                    hr2=int(hr2)+12
                if int(hr1) <10:
                    return f"0{hr1}:{min1} to {hr2}:{min2}"
                else:
                    return f"{hr1}:{min1} to {hr2}:{min2}"
            elif 'P' in pieces[2] and 'A' in pieces[5]:
                if pieces[3]=='12':
                    hr2='0'
                if pieces[0]=='12':
                    hr1='12'
                else:
                    hr1=int(hr1)+12
                if int(hr2)<10:
                    return f"{hr1}:{min1} to 0{hr2}:{min2}"
                else:
                    return f"{hr1}:{min1} to {hr2}:{min2}"
                
    else:
        raise ValueError



if __name__ == "__main__":
    main()
