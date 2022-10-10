def rev(a):
    s=0
    while a>0:
        rem=a%10
        s=(s*10)+rem
        a//=10
    return s
a=int(input())
arev=rev(a)
if a**2==rev(arev**2):
    print("True")
else:
    print("False")