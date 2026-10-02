# Project Installment 2,  Author: Carmen Rianna C. Rebamba

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

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
total = amount1 + amount2
average = (amount1 + amount2) / 2


print(f"\n{divider2}\nSUMMARY")

print(f"  - {item1}: \t\t${amount1}")
print(f"  - {item2}: \t\t${amount2}")
print(f"Total spent:\t\t${total}")
print(f"Average:\t\t${average}")

print(f"{divider2}")


print("Made by: Carmen Rianna C. Rebamba | Installment 2") 



