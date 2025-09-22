source_file = "source.txt"
destination_file = "destination.txt"
try:
    with open(source_file, 'r') as src:
        content = src.read()
    with open(destination_file, 'w') as dst:
        dst.write(content)
    print("File copied successfully.")
except FileNotFoundError:
    print(f"Error: The file '{source_file}' was not found.")