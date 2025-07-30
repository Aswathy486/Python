l=input("Enter list of numbers:")
list=list(map(int,l.split()))
print("List:",list)
even=[]
for i in list:
    if(i%2==0):
        even.append(i)
print("Even list: ",even)
