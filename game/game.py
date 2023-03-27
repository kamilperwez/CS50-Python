import random
n=0
while True:
    try:
        n=int(input('Level '))
        if n>0:
            break
        continue
    except:
        continue
val=random.randint(1,n)
guess=0
while guess !=val:
    try:
        guess=int(input('Guess :'))
        if guess > 0:
            if guess < val:
                print('Too small!')
                continue
            elif guess > val:
                print('Too large!')
                continue
            else:
                print('Just right!')
                continue
        else:
            continue
    except:
        continue