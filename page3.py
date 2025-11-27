from os import system
from rich import print
system ("clear || cls")
print("[bold yellow] On your first day of wand class you learn one of the three spells")

print("[bold yellow] If you want to learn the spell Expelliarmus the disarmming spell go to page 9")

print("[bold yellow] If you want to learn the spell Stupefy the stunning spell go to page 10")

print("[bold yellow] If you want to learn the spell Episkey the healing spell go to page 11")
choice = input("Where would you like to go to next?")
if choice == "9":
    import page9
if choice == "10":
    import page10
else:
    import page11