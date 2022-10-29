for _ in range(int(input())):
    x=int(input())
    c=bin(x)[2:]
    print(c.count("1"))