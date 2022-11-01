n=int(input())
l1=list(map(int,input().split()))
m=int(input())
l2=list(map(int,input().split()))
temp=[]
for i in l1:
    if i in l2:
      temp.append(i)  
if len(temp)==n:
    print(True)
else:
    print(False)