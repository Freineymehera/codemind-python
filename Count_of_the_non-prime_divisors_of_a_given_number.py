n=int(input())
i,k=1,1
c,d=0,0
while i<=n:
    if n%i==0:
        while k<=i:
            if i%k==0:
                c+=1
            k+=1
        if c!=2:
            d+=1
    c=0
    i+=1
    k=1
print(d)