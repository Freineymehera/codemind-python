n=int(input())
arr=list(map(int,input().split()))
k=int(input())
temp=[]
c=0
for i in arr:
    if arr.count(i)==k and i not in temp:
        temp.append(i)
if len(temp)==0:
    print(-1)
else:
    print(*temp)