n=int(input())
l=list(map(int,input().split()))
for i in l:
    print(i,end=' ')
if n%2==1:
    print(0)