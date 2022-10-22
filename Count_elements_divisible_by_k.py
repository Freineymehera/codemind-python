n,k=map(int,input().split())
arr=list(map(int,input().split()))
temp=[]
for i in range(len(arr)):
    if arr[i]%k==0:
        temp.append(arr[i])
    else:
        pass
print(len(temp))
        