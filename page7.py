from os import system
from rich import print
system ("clear || cls")
print("[bold green] You have brewed the strengh potion. But you accidently spilled the potion on yourself, and you break a whole table with the slightest touch")

print("[bold green] Will you, go to the headmaster for help? page 13 ")

print('[bold green} Or will you ask one of the students for help? page 14')
choice = input("Where will you go next?")
if choice == "13":
    import page13
else:
    import page14