print("===================================")
print("      Welcome to TripAdvise!")
print("   Basic Trip Budget Calculator")
print("===================================\n")

# --- User Inputs ---
print("Enter your estimated costs for the trip.\n")

# Use float() so users can enter decimals like 200.50
flights = float(input("Flights cost ($): "))
hotels = float(input("Hotel cost ($): "))
food = float(input("Food cost ($): "))
activities = float(input("Activities cost ($): "))
transport = float(input("Local transportation cost ($): "))

# Optional: number of trip days
days = int(input("\nHow many days is your trip? "))

# --- Calculations ---
total_cost = flights + hotels + food + activities + transport
daily_average = total_cost / days if days > 0 else 0

# --- Output ---
print("\n========= Trip Summary =========")
print(f"Flights:           ${flights:.2f}")
print(f"Hotels:            ${hotels:.2f}")
print(f"Food:              ${food:.2f}")
print(f"Activities:        ${activities:.2f}")
print(f"Transportation:    ${transport:.2f}")
print("---------------------------------")
print(f"Total Trip Cost:   ${total_cost:.2f}")
print(f"Daily Average:     ${daily_average:.2f} per day")
print("=================================\n")

print("Thank you for using TripAdvise!")
