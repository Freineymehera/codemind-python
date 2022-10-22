n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
temp=[]
for i in l1:
    if i in l2:
        if i not in temp:
            temp.append(i)
print(len(temp))