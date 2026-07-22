name = input("Enter your name: ")
surname = input("Enter your surname: ")
bio = input("Enter your bio: ")

# Username
username = f"{name[0]}{surname}"
print(f"Your username is: {username.lower()}")

#Full name
full_name = f"{name} {surname}"
print(f"Your full name is: {full_name.title()}")

# Removing space at the beginning and end 
bio = bio.strip()

# Replacing "i am" with "i'm"
bio = bio.replace("I am","I'm")

#Display bio
print(f"Your bio is: {bio}")

# Count characters
print(f"Yor bio has {len(bio)} characters.")

