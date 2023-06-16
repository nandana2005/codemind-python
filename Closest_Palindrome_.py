def fun(n):
    q=n
    s=0
    while q!=0:
        r=q%10
        s=s*10+r
        q=q//10
    if s==n:
        return 1
    else:
        return 0
n=int(input())
for i in range(n+1,2*n):
    if fun(i)==1:
        k=i
        break
for i in range(n-1,0,-1):
    if fun(i)==1:
        m=i
        break 
if abs(n-k)==abs(n-m):
    print(m,k)
elif abs(n-k)<abs(n-m):
    print(k)
else:
    print(m)
    