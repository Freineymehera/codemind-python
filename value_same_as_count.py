n=int(input())
x=list(map(int,input().split()))
temp=[]
c=0
for i in x:
    if x.count(i)==i and i not in temp:
        temp.append(i)
        c+=1
print(c)