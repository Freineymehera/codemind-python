t=int(input())
for i in range(t):
    n=input()
    sum=0
    l=list(n)
    l.reverse()
    for i in range(len(l)):
        sum+=int(l[i])*2**i
    print(sum)