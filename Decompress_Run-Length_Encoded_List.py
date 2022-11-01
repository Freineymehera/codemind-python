n=int(input())
l=list(map(int,input().split()))
for i in range(0,n,2):
    f=l[i]
    v=l[i+1]
    for j in range(f):
        print(v,end=" ")