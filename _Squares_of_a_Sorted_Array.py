n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in arr:
    l.append(i**2)
x=sorted(l)
print(*x)