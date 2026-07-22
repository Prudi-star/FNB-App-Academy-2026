# The concert Ticket Booker

welcome_message = "Welcome to the Concert Ticket Booker!"
print(welcome_message.upper())

print("Please fill in your details to book your tickets.")

# Getting user input
name = input("Enter your name: ")
surname = input("Enter your surname: ")

# Full name
full_name = f"{name} {surname}"

# Greeting
print(f"\nWelcome {full_name}!")

print("Please provide the following details for booking your tickets.")

# Collecting additional user information
date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")
id_number = int(input("Enter your ID number: "))
email = input("Enter your email address: ")
phone_number = int(input("Enter your phone number: "))

# Concert ticket details
concert_name = input("Enter the name of the concert you want to attend: ")
number_of_tickets = int(input("Enter the number of tickets you want to book: "))
ticket_type = input("Enter the type of ticket (VIP/Regular): ")
seating_preference = input("Enter your seating preference (Front/Back): ")
payment_method = input("Enter your preferred payment method (Credit Card/PayPal): ")

print("\nThank you for providing your details. Here is a summary of your booking:")
print(f"Concert: {concert_name}")
print(f"Tickets: {number_of_tickets}")
print(f"Ticket Type: {ticket_type}")
print(f"Seating Preference: {seating_preference}")
print(f"Payment Method: {payment_method}")

print("\nPlease review your details carefully before confirming your booking.")
print("If everything is correct, please proceed to payment.!")
payment_confirmation = input("Type 'yes' to confirm your booking and proceed to payment: ")
if payment_confirmation.lower() == 'yes':
    print("Processing your payment...")
    print("Payment successful! Your booking is confirmed.")
    print("Thank you for confirming your booking! Your tickets have been successfully booked.")
else:
    print("Booking not confirmed. Please restart the booking process if you wish to book tickets.")
    print("Thank you for visiting the Concert Ticket Booker. Have a great day!")