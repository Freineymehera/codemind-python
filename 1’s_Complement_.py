n=int(input())
a=bin(n)
b=(a[2:])
d=str(b)
s=''
for i in d:
    if i=='0':
        i='1'
        s+=i
    else:
        i="0"
        s+=i
t=int(s,2)
print(t)