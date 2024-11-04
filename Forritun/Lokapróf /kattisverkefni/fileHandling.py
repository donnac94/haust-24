# Write to file
with open("notes.txt", "w") as file: #  w = write
    file.write("This is a test file.") # Write to file

# Read and print content
with open("notes.txt", "r") as file: # r = read
    content = file.read() # Read file
    print("File content:", content) # Print file content
    