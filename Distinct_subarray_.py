n=int(input())
m=int(input())
s=0
for i in range(n,m+1):
    su=0
    for j in range(i,m+1):
        su+=j
        if su%2!=0:
            s+=1
print(s)