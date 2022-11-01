n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
arr=[]
for i in range(0,n):
    a=l1[i]+l2[i]
    arr.append(a)
print(*arr)