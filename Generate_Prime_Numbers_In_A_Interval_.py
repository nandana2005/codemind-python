def fun(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1        
n=int(input())
m=int(input())
for i in range(n+1,m+1):
    x=i
    if fun(x)==1:
        print(x)
    