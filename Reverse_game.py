def rev(n):
    temp=n
    reve=0
    while temp:
        reve=reve*10+temp%10
        temp//=10
    return reve
n=int(input())
x=list(map(int,input().split()))
for i in x:
    print(rev(i),end=" ")