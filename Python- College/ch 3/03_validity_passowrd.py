password = input("Enter a password: ")
valid = (len(password) >= 8 and
         any(char.isdigit() for char in password) and
         any(char.islower() for char in password) and
         any(char.isupper() for char in password) and
         any(char in "!@#$%^&*()" for char in password))
print("Valid Password" if valid else "Invalid Password")
