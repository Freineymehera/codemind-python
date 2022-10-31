n=int(input())
l=list(map(int,input().split()))
m=max(l)
s=0
for i in range(1,m//2):
    if (i*i) in l:
        s+=i*i
print(s)