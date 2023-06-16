def fun(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1        
n=int(input())
c=0
for i in range(2,n):
    if n%i==0:
        x=i
        if fun(x)==1:
            y=n//x
            if fun(y)==1:
                c=1
                print(x,y)
                break
if c==0:
    print("-1")
    