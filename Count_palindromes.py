def rev(n):
    temp=n
    reve=0
    while temp:
        reve=reve*10+temp%10
        temp//=10
    return reve
n=int(input())
x=list(map(int,input().split()))
c=0
for i in range(n):
    if x[i]==rev(x[i]):
        c+=1
print(c)