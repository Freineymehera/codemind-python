n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(0,n):
    if l[i]%2==0:
        s+=l[i]
    else:
        s+=0
print(s)