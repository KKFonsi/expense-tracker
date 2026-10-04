# Module 2 - Laboratory 3
# Installment 3: The Tracker Does Math
# Author: Kevin Kyle S. Alfon
# Description: Includes and calculates the expenses, tax, total, and budget.

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
item2 = input("What's your second item? ")
amount2 = float(input("What's the amount? "))
subtotal += amount2
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

average = subtotal / 2
tax = subtotal * (tax_percent / 100)
total = subtotal + tax
over_budget = total > budget
left = budget - total

print('\n' + '-' * 40)
print("SUMMARY")
print(f"  - {item1}:\t\t\t${amount1:.1f}")
print(f"  - {item2}:\t\t\t${amount2:.1f}")
print(f"Subtotal:\t\t\t${subtotal:.1f}")
print(f"Average:\t\t\t${average:.1f}")
print(f"Tax ({tax_percent:.1f}%):\t\t\t${tax:.1f}")
print(f"Grand total:\t\t\t${total:.1f}")
print(f"Over budget?\t\t\t{over_budget}")
print(f"Left in budget:\t\t\t${left:.1f}")
print('-' * 40)
print("Made by: Kevin Kyle S. Alfon | Installment 3")
