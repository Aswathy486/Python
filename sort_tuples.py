my_list=[1,2,3,3,2,4,5,5,6,3,2]
unique_elements=[]
for item in my_list:
    if item not in unique_elements:
        unique_elements.append(item)
print("unique elements",unique_elements)
