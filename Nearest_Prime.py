def fun(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1        
n=int(input())
for i in range(1,n+1):
    k=int(input())
    for i in range(k,2*k):
        if fun(i)==1:
            x=i
            break
    for i in range(k,0,-1):
        if fun(i)==1:
            y=i
            break
    if abs(k-x)==abs(k-y):
        print(y)
    elif abs(k-x)<abs(k-y):
        print(x)
    else:
        print(y)