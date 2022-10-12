n=int(input())
l=list(map(int,input().split()))
s1=s2=0
for i in range(0,n,2):
        s1+=l[i]
for i in range(1,n,2):
        s2+=l[i]
print(abs(s1-s2))