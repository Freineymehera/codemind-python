n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    if (l[i]%2==1) and (i%2==0):
        print("False")
        break
else:
    print(True)