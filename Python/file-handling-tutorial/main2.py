#Reading Files
with open("main.txt") as file:
    contents = file.read()
    print(contents)

#Writing to Files
with open("main.txt", mode="w") as file:
    file.write("New text.")
    
#Opening a File that doesn't exit in write mode will create it from scratch
with open("file_that_doesnt_exist.txt", mode="w") as file:
    file.write("New text.")