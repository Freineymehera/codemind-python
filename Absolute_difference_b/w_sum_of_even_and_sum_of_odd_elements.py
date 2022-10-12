n=int(input())
arr=list(map(int,input().split()))
s1=0
s2=0
for i in range(0,n):
    if arr[i]%2==0:
        s1+=arr[i]
    else:
        s2+=arr[i]
print(abs(s2-s1))