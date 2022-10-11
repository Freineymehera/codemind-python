def rev(n):
    s=0
    while n>0:
        rem=n%10
        s=(s*10)+rem
        n=n//10
    return s
a=int(input())  
if(a==rev(a)):
    print("True")
else:
    print("False")
    