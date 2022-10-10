n=int(input())
x=0
while (1):
    x=0
    while n>0:
        a=n%10
        x+=(a**2)
        n//=10
    if x<10:
        break
    else:
        n=x
        continue
if x==1 or x==7:
    print("True")
else:
    print("False")