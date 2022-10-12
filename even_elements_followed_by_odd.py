n=int(input())
l=list(map(int,input().split()))
arr=[]
for i in range(len(l)):
    if l[i]%2==0:
        arr.append(l[i])
for i in range(len(l)):
    if l[i]%2!=0:
        arr.append(l[i])
print(*arr)