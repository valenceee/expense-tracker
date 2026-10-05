# Project Installment 3,  Author: Carmen Rianna C. Rebamba

divider = ("=" * 40)
divider2 = ("-" * 40)

print(f"{divider}\n\tEXPENSE TRACKER\n\t\"Ang mahal\" to \"May Gcash?\"\n{divider}")

print("\nMAIN MENU")
print("  [1] Add an expense\t\t(coming soon)")
print("  [2] View all expenses\t\t(coming soon)")
print("  [3] Show total spent\t\t(coming soon)")
print("  [4] Exit\t\t\t(coming soon)\n")

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.\n")

subtotal = 0

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal = amount1

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2
average = (subtotal) / 2

tax_percent = float(input("Tax rate %? "))
tax = subtotal * (tax_percent * 0.01)
total = subtotal + tax

budget = float(input("Your budget? "))
over_budget = bool(budget < total)
left = (budget - total)


print(f"\n{divider2}\nSUMMARY")

print(f"  - {item1}: \t\t${amount1}")
print(f"  - {item2}: \t\t${amount2}")
print(f"Subtotal:\t\t${subtotal}")
print(f"Average:\t\t${average}")
print(f"Tax ({tax_percent}%):\t\t${tax}")
print(f"Grand Total:\t\t${total}")
print(f"Over budget?\t\t{over_budget}")
print(f"Left in budget:\t\t${left}")

print(f"{divider2}")


print("Made by: Carmen Rianna C. Rebamba | Installment 3") 



