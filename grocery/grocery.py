def getdict():
    gro={}
    while True:
        try:
            ip=input().upper()
            if ip not in gro:
                gro[ip]=1
            else:
                gro[ip]=gro[ip]+1
        except EOFError:
            break
    return gro
def main():
    grlist=getdict()
    sortedl=[x for x in grlist]
    sortedl.sort()
    for key in sortedl:
        print(grlist[key],key)
main()