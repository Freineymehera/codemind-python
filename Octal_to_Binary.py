a=['0','1','2','3','4','5','6','7']
b=['000','001','010','011','100','101','110','111']
for _ in range(int(input())):
    x=input()
    s=''
    for i in x:
        if i in a:
            c=a.index(i)
            s+=b[c]
    if x[0]=='1':
        print(s[2:])
    elif x[0]=='2' or x[0]=='3':
        print(s[1:])
    else:
        print(s)