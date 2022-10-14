n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
temp=[]
for i in l:
    if (i<a or i>b):
        temp.append(i)
if bool(len(temp)):
    print(min(temp))
else:
    print(-1)