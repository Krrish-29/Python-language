while (1): # The block keeps executing until the condition is true  
    #Body of the loop
    print("")

i = 0
while i < 5:
    print(" ")
    i = i + 1

l = [1, 7, 8]
for item in l:
    print(item)

# range(start, stop, step_size)
# step_size is usually not used with range()

for i in range(0,7): # range(7) can also be used.
    print(i) # prints 0 to 6

l= [1,7,8]
for item in l:
    print(item)
else:
    print("done")
for i in range (0,80):
    print(i)
    if i==3:
        break

for i in range(4):
    print("printing")
    if i == 2:
        continue
    print(i)

l = [1,7,8]
for item in l:
    pass