n=int(input())
l1=list(map(int,input().split()))
m=int(input())
l2=list(map(int,input().split()))
a=int(input())
c=0
for i in range(n):
    for j in range(i,i+1):
        if l1[i]<=a and l2[j]>=a:
            c+=1
        else:
            continue
print(c)