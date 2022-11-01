for _ in range(int(input())):
    n,m=map(int,input().split())
    l=list(map(int,input().split()))
    while m:
        x=l[n-1]
        for k in range(n-2,-1,-1):
            l[k+1]=l[k]
        l[0]=x
        m-=1
    print(*l)