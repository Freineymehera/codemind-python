s=input()
vo="aeiouAEIOU"
l=[]
for i in s:
    if i in vo:
        l.append(i)
print(len(l))