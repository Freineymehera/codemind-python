a,b=map(int,input().split())
n=list(map(int,input().split()))
m=list(map(int,input().split()))
temp=[]
for i in n:
    if i not in m:
        if i not in temp:
            temp.append(i)
for i in m:
    if i not in n:
        if i not in temp:
            temp.append(i)
print(*temp)