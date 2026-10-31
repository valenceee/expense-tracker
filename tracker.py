# Project Installment 5,  Author: Carmen Rianna C. Rebamba

divider = ("=" * 40)
divider2 = ("-" * 40)

print(f"{divider}\n\tEXPENSE TRACKER\n\t\"Ang mahal\" to \"May Gcash?\"\n{divider}")

name = input("What's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
print(f"Welcome, {name}!")

print("\nMAIN MENU")
print("  [1] Add an expense")
print("  [2] View all expenses\t\t(coming soon)")
print("  [3] Show total spent")
print("  [4] Exit\n")

choice = 0
subtotal = 0
count = 0


while choice != "4":
    choice = input("Choose 1-4: ") 

    if choice == "1":
        amount = float(input("Amount? "))
        
        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")

        count += 1
        subtotal += amount
        
    elif choice == "2":
        print("  Coming soon: the tracker can't remember each item yet.")

    elif choice == "3":
        tax = subtotal * (tax_percent * 0.01)
        total = subtotal + tax
        over_budget = bool(budget < total)
        left = (budget - total)
        print(f"  Expenses:\t{count}")
        print(f"  Subtotal:\t${subtotal}")
        print(f"  Tax ({tax_percent}%):\t${tax}")
        print(f"  Grand Total:\t${total}")
        if over_budget:
            print(f"  Overbudget by ${(total - budget)}!")
        elif total >= (0.9 * budget): 
            print(f"  Careful: Only ${(left)} left.")
        else: 
            print(f"  Within budget. ${(left)} left.")
    elif choice == "4":
        break
    else:
        print("  Please choose 1, 2, 3, or 4.")

print(f"Goodbye, {name}!")
    


print(f"{divider2}")
print("Made by: Carmen Rianna C. Rebamba | Installment 5") 
print(f"{divider}")


