# Module 3 - Laboratory 5
# Installment 5: The Menu Comes Alive
# Author: Kevin Kyle S. Alfon
# Description: A menu-driven expense tracker that records expenses, calculates totals and taxes, and evaluates spending against a budget.

choice = ""
subtotal = 0.00
count = 0

print('=' * 40)
print("EXPENSE TRACKER".center(40))
print("Every peso counts".center(40))
print('=' * 40)

name = input("\nWelcome, what should we call you? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget ($)? "))

print(f"\nWelcome, {name}!")

while choice != "4":
    print("\nMAIN MENU")
    print("  [1] Add an expense")
    print("  [2] View all expenses\t\t(coming soon)")
    print("  [3] Show total spent")
    print("  [4] Exit")

    choice = input("\nChoose 1-4: ")

    if choice == "1":
        amount = float(input("\nWhat's the amount ($)? "))
        subtotal += amount
        count += 1

        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")

    elif choice == "2":
        print("\n  Coming soon: the tracker can't remember each item yet.")

    elif choice == "3":
        tax = subtotal * (tax_percent / 100)
        total = subtotal + tax
        over_budget = total > budget
        left = budget - total

        print('\n' + '-' * 40)

        print("SUMMARY")
        print(f" Expenses:\t\t{count}")
        print(f" Subtotal:\t\t${subtotal:.1f}")
        print(f" Tax ({tax_percent:.1f}%):\t\t${tax:.1f}")
        print(f" Grand total:\t\t${total:.1f}")

        if over_budget:
            print(f" Over budget by ${abs(left):.1f}!")
        elif total > budget * 0.90:
            print(f" Careful: only ${left:.1f} left.")
        else:
            print(f" Within budget. ${left:.1f} left.")

        print('-' * 40)

    elif choice == "4":
        print(f"\nGoodbye, {name}!")
        print('-' * 40)
        print("Made by: Kevin Kyle S. Alfon | Installment 5")
        print('=' * 40)

    else:
        print("\n  Please choose 1, 2, 3, or 4.")