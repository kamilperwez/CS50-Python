def main():
    tm=input('What time is it? ').strip()
    nt=convert(tm)
    if(nt>=7 and nt<=8):
        print('breakfast time')
    elif(nt>=12 and nt<=13):
        print('lunch time')
    elif(nt>=18 and nt<=19):
        print('dinner time')
def convert(time):
    i=time.split(':')
    return (float(i[0])+(round(float(i[1])/60,1)))
main()