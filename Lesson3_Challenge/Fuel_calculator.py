# African Fuel Calculator

# Ask user how many kilometers they want to drive
distance = float(input("Enter the distance to be traveled (in kilometers): "))

# Petrol price needed per litre
fuel_efficiency = float(input("Enter the petrol efficiency of your vehicle (in kilometers per liter): "))

fuel_needed = distance / fuel_efficiency
print(f"The amount of petrol needed is: {fuel_needed:.1f} liters")

Petrol_price = float(input("Enter the price of petrol per liter (in R): "))

# total cost calculation
total_cost = fuel_needed * Petrol_price
print(f"The total cost of petrol is: R {total_cost:.1f}")

print("Thank you for using the African Petrol Calculator!")