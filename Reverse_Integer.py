n=int(input())
p=str(abs(n))
num=p[::-1]
numb=int(num)
if n<0:
    print(numb*-1)
else:
    print(numb)