def fun(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1        
n=int(input())
m=int(input())
f=n+m
for i in range(1,f+1):
    k=f+i
    if fun(k)==1:
        print(i)
        break
        