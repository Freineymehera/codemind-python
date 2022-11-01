n=int(input())
a=list(map(int,input().split()))
res=1
l=[]
for i in a:
    res*=i
for i in a:
    l.append(res//i)
for i in l:
    print(i,end=" ")