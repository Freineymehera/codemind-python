n=int(input())
arr=list(map(int,input().split()))
s=0
for x in arr:
    if x%2!=0:
        s+=x
print(s)