n=int(input())
c=[]
while n>0:
    a=n%10
    c.append(a)
    n//=10
print(max(c))