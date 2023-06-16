n=int(input())
k=str(n)
while n!=0:
    r=n%10
    x=k.count(str(r))
    if x!=1:
        print('Not Unique Number')
        break
    n=n//10    
else:
    print("Unique Number")