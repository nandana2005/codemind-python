n=int(input())
for i in range(1,n+1):
    a=int(input())
    p=a
    s=0
    while(p!=0):
        r=p%10
        s=s*10+r
        p=p//10
    if s==a:
        print(True)
    else:
        print(False)
        