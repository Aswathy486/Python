f1= "file1.txt"
f2= "file2.txt"
f3= "merged.txt"
try:
    with open("file1.txt", 'r') as f1, open("file2.txt", 'r') as f2:
        content1 = f1.read()
        content2 = f2.read()
    with open("merged.txt", 'w') as f3:
        f3.write(content1 + "\n" + content2)
    print(f"Content of '{f1}' and '{f2}' are successfully merged to {f3}")
except FileNotFoundError:
    print(f"Error: The file '{f1}' and '{f2}' was not found.")