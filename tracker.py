# Module 3 - Laboratory 4
# Installment 4: The Tracker Makes Decisions
# Author: Kevin Kyle S. Alfon
# Description: Tracks two expenses which will provide spending warnings and budget decisions.

subtotal = 0.00

print('=' * 40)
print("EXPENSE TRACKER".center(40))
print("Every peso counts".center(40))
print('=' * 40)
print("\nMAIN MENU")
print("  [1] Add an expense\t\t(coming soon)")
print("  [2] View all expenses\t\t(coming soon)")
print("  [3] Show total spent\t\t(coming soon)")
print("  [4] Exit\t\t\t(coming soon)\n")

name = input("\nWelcome, what should we call you? ")
print(f"Welcome, {name}! Let's log two expenses.\n")

item1 = input("What's your first item? ")
amount1 = float(input("What's the amount? "))
subtotal += amount1
if amount1 > 200:
    print("  Huge expense - are you sure?")
elif amount1 > 100:
    print("  Big expense.")
elif amount1 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

item2 = input("What's your second item? ")
amount2 = float(input("What's the amount? "))
subtotal += amount2
if amount2 > 200:
    print("  Huge expense - are you sure?")
elif amount2 > 100:
    print("  Big expense.")
elif amount2 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")
    
if amount1 > 100 and amount2 > 100:
    print("  Two big expenses in a row - slow down!")

tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

average = subtotal / 2
tax = subtotal * (tax_percent / 100)
total = subtotal + tax
over_budget = total > budget
left = budget - total

print('\n' + '-' * 40)

print("SUMMARY")
print(f"  - {item1}:\t\t${amount1:.1f}")
print(f"  - {item2}:\t\t${amount2:.1f}")

print(f"Subtotal:\t\t${subtotal:.1f}")
print(f"Average:\t\t${average:.1f}")
print(f"Tax ({tax_percent:.1f}%):\t\t${tax:.1f}")
print(f"Grand total:\t\t${total:.1f}")

if over_budget:
    print(f"Over budget by ${abs(left):.1f}!")
elif total > budget * 0.90:
    print(f"Careful: only ${left:.1f} left.")
else:
    print(f"Within budget. ${left:.1f} left.")

print('-' * 40)
print("Made by: Kevin Kyle S. Alfon | Installment 4")
