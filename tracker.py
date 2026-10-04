# Module 0 - Laboratory 1
# Installment 2: Talking to the User
# Author: Kevin Kyle S. Alfon
# Description: Collects and summarizes input from user for two expenses.

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
item2 = input("What's your second item? ")
amount2 = float(input("What's the amount? "))

total = amount1 + amount2
average = total / 2

print()
print('-' * 40)
print("SUMMARY")
print(f"{f'  - {item1}:':<28}₱{amount1:.2f}")
print(f"{f'  - {item2}:':<28}₱{amount2:.2f}")
print(f"{'TOTAL SPENT:':<28}₱{total:.2f}")
print(f"{'Average:':<28}₱{average:.2f}")
print('-' * 40)
print(f"Made by: {name} | Installment 2")
