a=int(input())
b=int(input())
for i in range(a,b+1):
    n=i
    c=0
    s=0
    while i:
        d=i%10
        i=i//10
        c+=1
        if d!=0:
            if n%d==0:
                s+=1
    if s==c:
            print(n,end=' ')