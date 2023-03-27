import random


def main():
    level=get_level()
    score=0
    for i in range(1,11):
        x,y=generate_integer(level)
        for k in range(1,4):
             try:
                 ans=int(input('{} + {} = '.format(x,y)))
                 if ans==(x+y):
                     score=score+1
                     break
                 else:
                     print('EEE')
             except:
                 print('EEE')
             if k==3:
                 print(('{} + {} = '.format(x,y)),(x+y))
    print('Score: ',score)
def get_level():
    lvl=0
    while True:
        try:
            lvl=int(input('Level :'))
            if lvl ==1 or lvl==2 or lvl ==3:
                return lvl
            else:
                continue
        except:
            continue
def generate_integer(level):
    if level ==1:
        x=random.randint(0,9)
        y=random.randint(0,9)
    elif level ==2:
        x=random.randint(10,99)
        y=random.randint(10,99)
    elif level ==3:
        x=random.randint(100,999)
        y=random.randint(100,999)
    return x,y

if __name__ == "__main__":
    main()
