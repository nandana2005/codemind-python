def fun(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1        
n=int(input())
c=2
for i in range(2,n):
    if n%i==0:
        x=i
        if fun(x)==0:
            c=c+1
print(c)    
            
        