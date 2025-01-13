# 7.1 Create, write, read:
with open("practice.txt", "w") as f:
    f.write("Problem solving")
with open("practice.txt", "r") as f:
    print(f.read())
    
# 7.2 Append to a file:
with open("practice.txt", "a") as f:
    f.write("\nAdding a new text sentence")
with open("practice.txt", "r") as f:
    print(f.read())

# 7.3 Count lines:
with open("test.txt", "r") as f:
    print(len(f.readlines()))