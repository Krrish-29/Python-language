#write a program to uppercase half string
def upper_half_string(string):
    x=string[0:int((len(string)/2)+1)]
    return x.upper()+string[int((((len(string))/2))+1):];
y=input("Enter a String:")
print(f"The new string is {upper_half_string(y)}")
