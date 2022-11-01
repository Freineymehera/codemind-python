n=int(input())
l=[n]
l=list(map(int,input().split()))
c=co=0
ma=0
for i in range(n):
    c=0
    for j in range(n):
        if i!=j:
            if l[i]==l[j]:
                c=1
                break
    if c==1:
        continue
    else:
        if ma<l[i]:
            ma=l[i]
            co+=1
if co>0:
    print(ma)
else:
    print(-1)