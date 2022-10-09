n=int(input())
a=n*n
r=0
while a>0:
    b=a%10
    r+=b
    a=a//10

if(r==n):
    print("Neon Number")
else:
    print("Not Neon Number")