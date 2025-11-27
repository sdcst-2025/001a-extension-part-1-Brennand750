from os import system
from rich import print
system ("clear || cls")
print("[bold blue] If you picked the beast classes, Today in class you are researching about a hippogriff")

print("[bold blue] Will you pet the hippogriff or will you be scared of it and stand back?")

print("[bold blue] If you stand back go to page 5")

print("[bold blue] If you pet the hippogriff go to page 12")
choice = input("Where would you like to go to next?")
if choice == "5":
    import page5
else:
    import page12