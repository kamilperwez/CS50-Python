months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"]
def chkdate(prompt):
    while True:
        dte=input(prompt)
        try:
            if '/' in dte:
                month,day,year=dte.split('/')
                if int(month)>=1 and int(month)<=12 and int(day)<=31:
                    print(f'{int(year)}-{int(month):02}-{int(day):02}')
                    break
                else:
                    continue
            elif ',' in dte:
                dte=dte.replace(',','')
                month,day,year=dte.split(' ')
                if month in months:
                    month=months.index(month)+1
                    if int(month)>=1 and int(month)<=12 and int(day)<=31:
                        print(f'{int(year)}-{int(month):02}-{int(day):02}')
                        break
                    else:
                        continue
                else:
                     continue
        except:
            continue

def main():
    chkdate('Date: ')
main()
