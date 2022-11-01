n=int(input())
arr=list(map(int,input().split()))
a=int(input())
f=0
s=0
for i in range(len(arr)):
    if arr[i]==a:
        f=i
        s+=1
if s==0:
    print(-1)
else:
    print(f)