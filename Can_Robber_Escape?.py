n=int(input())
c=0
arr=list(map(int,input().split()))
for i in range(len(arr)):
    if arr[i]%2!=0:
        c=c+1
if c<=2:
    print("YES")
else:
    print("NO")