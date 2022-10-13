n=int(input())
arr=list(map(int,input().split()))
l=0
for i in range(len(arr)):
    if arr[i]==0 or arr[i]==1:
        l+=1
        i+=1
    else:
        break
if l==n:
    print("True")
else:
    print("False")
        