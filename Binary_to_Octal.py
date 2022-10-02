for _ in range(int(input())):
    n=int(input())
    b=[0,1,10,11,100,101,110,111]
    i=[]
    while n!=0:
        r=n%1000
        i.append(b.index(r))
        n=n//1000
    i.reverse()
    for ele in i:
        print(ele,end="")
    print()