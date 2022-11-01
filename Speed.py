t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    c=1
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            c+=1
    print(c)
    