n=int(input())
l=list(set(map(int,input().split())))
s=0
for i in l:
    s+=i
print(s)