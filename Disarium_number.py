n=int(input())
N=str(n)
M=N[::-1]
m=int(M)
k=1
s=0
while True:
    r=m%10
    s=s+(r**k)
    if m==0:
        break
    k+=1
    m=m//10
if n==s:
    print("True")
else:
    print("False")
    