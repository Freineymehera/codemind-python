n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    while i!=0: 
        if i>0:
            d=i%10
            s+=d
            i//=10
print(s)