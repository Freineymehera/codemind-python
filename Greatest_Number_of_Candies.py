n=int(input())
l=list(map(int,input().split()))
m=int(input())
temp=[]
x=max(l)
for i in range(len(l)):
    if l[i]+m>=x:
        temp.append(True)
    else:
        temp.append(False)
print(*temp)