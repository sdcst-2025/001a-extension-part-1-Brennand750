from os import system
from rich import print
system ("clear || cls")
print("[bold yellow] For today's lesson you will learn the Expelliarmus spell using your wand.")

print('[bold yellow] When you used this spell, you accidently used it on a student sending his wand into the air and made it stuck to the ceiling')

print('[bold yellow] To get the wand down do you go to the headmaster for help? page 13')

print('[bold yellow] Or do you ask a student for help? page 14')
choice = input("Where would you like to go to next?")
if choice == "13":
    import page13
else:
    import page14