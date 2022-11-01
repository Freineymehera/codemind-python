n=int(input())
l=list(map(int,input().split()))
a=[]
c=0
for i in range(n):
    if l[i]==0:
        c+=1
    else:
        a.append(l[i])
for i in range(c):
    a.append(0)
print(*a)