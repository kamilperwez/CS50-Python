flnm=input('File name: ').strip().lower()
i=flnm.rfind('.')
ext=flnm[i::]
match(ext):
    case '.gif' : print('image/gif')
    case '.jpg'|'.jpeg' : print('image/jpeg')
    case '.png' : print('image/png')
    case '.pdf' : print('application/pdf')
    case '.txt' : print('text/plain')
    case '.zip' : print('application/zip')
    case _: print('application/octet-stream')


