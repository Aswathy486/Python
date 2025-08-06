text=input("Enter string")
w=text.split()
d={}
for i in w:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
