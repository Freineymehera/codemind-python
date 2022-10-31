n=int(input())
l=list(map(int,input().split()))
num=0
for i in l:
    num=(num*10)+i
num+=1
l2=[]
while num>0:
    rem=num%10
    l2.append(rem)
    num//=10
l2.reverse()
for i in l2:
    print(i,end=" ")