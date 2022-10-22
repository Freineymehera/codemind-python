n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l1=set(l1)
l2=set(l2)
temp=[]
for i in l1:
    if i not in l2:
        if i not in temp:
            temp.append(i)
for i in l2:
    if i not in l1:
        if i not in temp:
            temp.append(i)
print(len(temp))