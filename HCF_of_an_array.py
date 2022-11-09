n=int(input())
l=list(map(int,input().split()))
mi=l[0]
j=1
while j<n:
    if l[j]%mi==0:
        j+=1
    else:
        mi=l[j]%mi
print(mi)