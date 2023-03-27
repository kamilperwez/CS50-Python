def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s)<2 or len(s)>6:
        return False
    elif s[0:2:].isalpha()!=True:
        return False
    elif s[2::].isalnum()!=True and len(s)>2:
        return False

    for i in [2,3,4,5]:
        try:
            if s[i].isdigit() and len(s)<=i+1:
                if s[i-1]=='0' and s[i]!='0' and s[i-2].isalpha():
                    return False
                else:
                    return True
            elif s[i].isalpha() and s[i-1].isdigit():
                return False
            elif s[i].isdigit() and len(s)>i+1:
                if s[i-1]=='0':
                    return False
        except:
            continue
    return True


if __name__ == "__main__":
    main()
