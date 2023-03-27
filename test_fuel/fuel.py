def main():
    frac = input("Fraction: ")
    pct = convert(frac)
    print(gauge(pct))

def convert(fraction):
    try:
        x,y=fraction.split('/')
        x=int(x)
        y=int(y)
        f=x/y
        if x>y:
             raise ValueError
    except ValueError:
         raise ValueError
    except ZeroDivisionError:
         raise ZeroDivisionError
    else:
        return (round(f*100))


def gauge(percentage):
    if percentage <=1:
        return 'E'
    elif percentage >=99:
        return 'F'
    else:
        return (f'{percentage}%')


if __name__ == "__main__":
    main()
