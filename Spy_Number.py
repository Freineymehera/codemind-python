n=int(input())
c=n
s=0
r=1
while n:
    d=n%10
    n=n//10
    s+=d
    r=r*d
if r==s:
    print("Spy Number")
else:
    print("Not Spy Number")