from os import system
from rich import print
system ("clear || cls")
print("[bold green] On your first day of potions pick a potion you want to create")

print("[bold green] If you want to brew a invisablity potion go to page 6") / ("If you want to brew a strengh potion go to page 7") / ("If you want to brew a flight potion go to page 8")
choice = input("Where would you like to go to next?")
if choice == "6":
    import page6
if choice == "7":
    import page7
else:
    import page8