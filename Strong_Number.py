def fun(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f    
    
n=int(input())
s=0
p=n
while(p!=0):
    r=p%10
    x=fun(r)
    s=s+x
    p=p//10
if s==n: 
    print('The number',n,'is a strong number')
else:
    print('The number',n,'is not a strong number')
    