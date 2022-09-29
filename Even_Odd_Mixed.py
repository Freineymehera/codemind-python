n=int(input())
f=0
e=0
o=0
while n!=0:
    f+=1
    v=n%10
    n=n//10
    if v%2==0:
        e+=1
    else:
        o+=1
if e==f:
    print("Even")
elif o==f:
    print("Odd")
else:
    print("Mixed")
    