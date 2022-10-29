n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
for i in b:
    if i in a:
        c+=1
        z=a.index(i)
        a.pop(z)
    else:
        break
if c==len(b):
    print("Yes")
else:
    print("No")