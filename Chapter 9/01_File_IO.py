# open("filename", "mode of opening(read mode by default)")
open("this.txt", "r")
# Open the file in read mode
f = open("this.txt", "r")
# Read its contents
text = f.read()
# Print its contents
print(text)
# Close the file
f.close()
f.readline() # Read one line from the file.
'''
r - open for reading
w - open for writing
a - open for appending
+ - open for updating.
'rb' will open for read in binary mode.
'rt' will open for read in text mode.
'''
# Open the file in write mode
f = open("this.txt", "w")
# Write a string to the file
f.write("this is nice")
# Close the file
f.close()
# Open the file in read mode using 'with', which automatically closes the file
with open("this.txt", "r") as f:
# Read the contents of the file
    text = f.read()
# Print the contents
print(text)