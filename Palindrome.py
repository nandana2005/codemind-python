n=int(input())
p=str(n)
q=int(p[::-1])
if n==q:
    print(True)
else:
    print(False)