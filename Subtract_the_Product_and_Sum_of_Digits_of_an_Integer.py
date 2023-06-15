n=int(input())
p=str(n)
c=0
q=1
for i in p:
    i=int(i)
    c+=i
    q*=i
print(q-c)