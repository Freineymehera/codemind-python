n=int(input())
l=[n]
l=list(map(int,input().split()))
e=0
o=0
for i in range(n):
    if i%2==0:
        e+=l[i]
    else:
        o+=l[i]
if e==o:
    print("YES")
else:
    print("NO")