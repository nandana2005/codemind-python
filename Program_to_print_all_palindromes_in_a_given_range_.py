def fun(n):
    s=0
    while(n!=0):
        r=n%10
        s=s*10+r
        n=n//10
    return s    
a=int(input())
b=int(input())
for i in range(a,b+1):
    x=fun(i)
    if(x==i):
        print(x,end=" ")