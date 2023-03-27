import requests
import sys
try:
    i=float(sys.argv[1])
    r=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    q=r.json()
    k1=q['bpi']
    k2=k1['USD']['rate_float']
    amt=i*k2
    print('${:,.4f}'.format(amt))
except ValueError:
    print('Not a number')
    sys.exit(1)
except IndexError:
    print('No Command Line Data')
    sys.exit(1)
except:
    print('Command Line Error')
