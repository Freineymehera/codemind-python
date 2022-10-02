t=int(input())
for i in range(t):
    n=int(input())
    i=[]
    while n!=0:
        r=n%2
        i.append(r)
        n=n//2
    i.reverse()
    for ele in i:
        print(ele,end='')
    print()