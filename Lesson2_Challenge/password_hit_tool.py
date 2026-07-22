# The secure passward hint tool

# Password input
password = input("Enter your password: ")

# Spaces clean-up
password = password.strip()

# First and last letter password
first_letter = f"{password[0]}"
last_letter = f"{password[-1]}"

# Printing a hint
print(f"Your password hint:{first_letter.upper()} and ends with {last_letter.upper()}.")