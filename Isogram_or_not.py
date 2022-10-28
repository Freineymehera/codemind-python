s=input()
a=''
for i in s:
    if i not in a:
        a+=i
if len(a)==len(s):
    print(True)
else:
    print(False)