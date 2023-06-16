def fun(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1        
n=int(input())
s=0
q=n
while(q!=0):
    r=q%10
    s=s*10+r
    q=q//10
if fun(n)==1 and fun(s)==1:
    print("circular prime")
elif fun(n)==1 and fun(s)!=1:
    print("prime but not a circular prime")
else:
    print("not prime")