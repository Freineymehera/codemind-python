n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
temp=[]
flag=0
for i in range(n):
    if l[i]>=a and l[i]<=b:
        temp.append(l[i])
        flag=1
if flag!=1:
    print(-1)
else:
    print(min(temp))