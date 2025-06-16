file = open("main.txt", "w")
file.write("Hello, World!\n")
file.write("I am learning Python!")
file.close()

with open("main.txt", "r") as f:
    content = f.readlines()
    print(content)



file = open("main.txt", "r")
content = file.readlines()
print(content)
file.close()