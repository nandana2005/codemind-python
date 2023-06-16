n=int(input())
a=0
b=1
while b<n:
    c=a+b  
    a=b  
    b=c  
if abs(n-a)==abs(n-b):
    print(a,b)
elif abs(n-a)<abs(n-b):
    print(a)
else:
    print(b)