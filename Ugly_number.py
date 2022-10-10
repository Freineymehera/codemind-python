def isUgly(n):
    if n<=0:
        return "Not Ugly Number"
    while n>0:
        if n==1:
            return "Ugly Number"
        elif n%2==0:
            n//=2
        elif n%3==0:
            n//=3
        elif n%5==0:
            n//=5
        else:
            return "Not Ugly Number"
        return "Ugly Number"
n=int(input())
print(isUgly(n))