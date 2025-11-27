from os import system
from rich import print
system ("clear || cls")
print("[bold green] You have created the invisability spell, but you accidentally spilled it on yourself ")

print("[bold green] What will you do?")

print("[bold green] Will you go to see the head master on page 13, or will you ask another student for help on page 14.")
choice = input("Where do you want to go?")
if choice == "13":
    import page13
else:
    import page14