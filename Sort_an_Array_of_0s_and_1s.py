n=int(input())
arr=list(map(int,input().split()))
for i in range(0,n):
    if arr[i]==0:
        print(arr[i],end=" ")
for i in range(n):
    if arr[i]==1:
        print(arr[i],end=" ")