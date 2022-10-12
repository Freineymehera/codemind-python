n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(0,n):
    s+=l[i]
a=s//n
if a in l:
    print("True")
else:
    print("False")