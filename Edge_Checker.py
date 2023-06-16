n,m=map(int,input().split())
if n==1 and m==10 or m==1 and n==10:
    print('Yes')
elif (abs(n-m))==1:
    print('Yes')
else:
    print("No")