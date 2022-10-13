n=int(input())
l=list(map(int,input().split()))
s=0
k=len(l)-1
for i in range(len(l)):
    s+=((2**k)*l[i])
    k-=1
print(s)