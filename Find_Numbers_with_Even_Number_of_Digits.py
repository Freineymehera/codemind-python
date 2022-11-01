n=int(input())
l=list(map(int,input().split()))
x=[str(x) for x in l]
c=0
m=[]
for i in x:
    res=len(i)
    m.append(res)
for i in m:
    if i%2==0:
        c=c+1
print(c)