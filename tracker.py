# Project Installment 4,  Author: Carmen Rianna C. Rebamba

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

if amount1 > 200:
    print("  Huge expense - are you sure?")
elif amount1 > 100:
    print("  Big expense.")
elif amount1 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

subtotal = amount1

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

if amount2 > 200:
    print("  Huge expense - are you sure?")
elif amount2 > 100:
    print("  Big expense.")
elif amount2 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

if amount1 > 100 and amount2 > 100:
    print("Two big expenses in a row - slow down!")

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
if over_budget:
    print(f"Overbudget by ${(total - budget)}!")
elif total >= (0.9 * budget): 
    print(f"Careful: Only ${(left)} left.")
else: 
    print(f"Within budget. ${(left)} left.")

print(f"{divider2}")


print("Made by: Carmen Rianna C. Rebamba | Installment 4") 



