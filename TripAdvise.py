import csv

print("======================================")
print("        Welcome to TripAdvise!        ")
print("      Basic Trip Budget Calculator    ")
print("======================================\n")

# --- User Inputs ---
print("Enter your estimated costs for the trip.\n")

# Flights & lodging
flights = float(input("Flights cost ($): "))
hotel_per_night = float(input("Hotel cost per night ($): "))
nights = int(input("How many nights are you staying? "))

# Food
food_per_day = float(input("Estimated food cost per day ($): "))

# Activities (multiple)
activities_total = 0
num_activities = int(input("How many paid activities? "))

for i in range(num_activities):
    cost = float(input(f"  Cost of activity #{i+1} ($): "))
    activities_total += cost

# Transportation
transport = float(input("Local transportation cost ($): "))

# Trip length
days = int(input("\nHow many days is your trip? "))

# Ask for a budget goal
budget = float(input("\nWhat is your total trip budget ($)? "))


# --- Calculations ---
hotel_total = hotel_per_night * nights
food_total = food_per_day * days

total_cost = flights + hotel_total + food_total + activities_total + transport
daily_average = total_cost / days if days > 0 else 0

difference = budget - total_cost
if difference > 0:
    budget_message = f"You are ${difference:.2f} UNDER budget! Great job!"
elif difference < 0:
    budget_message = f"You are ${-difference:.2f} OVER budget! 😬"
else:
    budget_message = "You hit your budget exactly!"


# --- Output Summary ---
print("\n========== Trip Summary ==========")
print(f"Flights:             ${flights:.2f}")
print(f"Hotel ({nights} nights): ${hotel_total:.2f}")
print(f"Food ({days} days):    ${food_total:.2f}")
print(f"Activities:          ${activities_total:.2f}")
print(f"Transportation:      ${transport:.2f}")
print("----------------------------------")
print(f"Total Trip Cost:     ${total_cost:.2f}")
print(f"Daily Spending Avg:  ${daily_average:.2f} per day")
print("----------------------------------")
print(budget_message)
print("==================================\n")

print("Thank you for using TripAdvise!")

# --- Optional CSV Export ---
save_csv = input("\nWould you like to export this summary as a CSV file? (y/n): ").lower()

if save_csv == "y":
    with open("trip_summary.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Cost ($)"])
        writer.writerow(["Flights", flights])
        writer.writerow(["Hotel", hotel_total])
        writer.writerow(["Food", food_total])
        writer.writerow(["Activities", activities_total])
        writer.writerow(["Transportation", transport])
        writer.writerow(["Total Cost", total_cost])
        writer.writerow(["Daily Average", daily_average])
        writer.writerow(["Budget Difference", difference])

    print("CSV file saved as: trip_summary.csv 🚀")
