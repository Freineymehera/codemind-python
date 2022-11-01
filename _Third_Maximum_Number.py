n=int(input())
l=list(set(map(int,input().split())))
arr=[]
arr=sorted(list(set(l)))
if n>=3:
    print(arr[-3])
else:
    print(max(arr))
    