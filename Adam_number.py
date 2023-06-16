n=int(input())
s=n*n
k=m=0
while(n!=0):
    k=k*10+(n%10)
    n=n//10
q=k*k
while(q!=0):
    m=m*10+(q%10)
    q=q//10
if m==s:
    print(True)
else:
    print(False)
    