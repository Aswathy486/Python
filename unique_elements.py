l=input("Enter list of numbers")
my_list=list(map(int,l.split()))
unique_elements=[]
for item in my_list:
    if item not in unique_elements:
        unique_elements.append(item)
print("unique elements",unique_elements)
