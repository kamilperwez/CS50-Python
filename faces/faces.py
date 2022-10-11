def convert(msg):
    return msg.replace(':)','🙂').replace(':(','🙁')
def main():
    txt=input('Enter a Message ')
    print(convert(txt))
main()