def fun(n):
    q=n
    while q!=0:
        r=q%10
        if r==0:
            return 0
        elif n%r!=0:
            return 0
        q=q//10
    return 1    
n=int(input())
m=int(input())
for i in range(n,m+1):
    if fun(i)==1:
        print(i,end=" ")