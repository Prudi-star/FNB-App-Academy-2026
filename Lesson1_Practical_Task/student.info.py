print("Welcome student, Please fill in your Personal Information.\n")

# Collect user information
name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
favorite_number = int(input("Enter your favorite number: "))

# Full name
full_name = f"{name} {surname}"

# Greeting
print(f"\nWelcome {full_name}!")

# String manipulation
print(f"Name in uppercase: {full_name.upper()}")
print(f"Name in Title case: {full_name.title()}")

# Arithmetic 
age_in_months = age * 12
print(f"Age in months is: {age_in_months}")

# Round favorite number
rounded_favorite_number = round(favorite_number , 2)
print(f"Favorite number rounded to 2 decimal places is: {rounded_favorite_number}")

