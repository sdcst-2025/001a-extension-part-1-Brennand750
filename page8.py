from os import system
from rich import print
system ("clear || cls")
print('[bold green] You brew the flight potion. But you accidently pour it on yourself, and you start to float in the air')

print('[bold green] Will you go to the head master for help? page 13')

print('[ bold green] Or do you ask one of the students for help? page 14')
choice = input("Where would you like to go to next?")
if choice == "13":
    import page13
else:
    import page14