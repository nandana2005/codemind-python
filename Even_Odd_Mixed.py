a=int(input())
e=0
o=0
p=str(a)
for i in p:
    i=int(i)
    if i%2==0:
        e+=1
    else:
        o+=1
if e==0:
    print("Odd")
elif o==0:
    print("Even")
else:
    print("Mixed")