from os import system
from rich import print
system ("clear || cls")
print('[bold blue] You closely and slowly go up to the hippogriff and then right after it get starled and kicks you.')

print('[bold blue] Do you go see the head master for help? page 13')

print('[bold blue] Or do you ask a student for help? page 14')
choice = input("Where would you like to go to next?")
if choice == "13":
    import page13
else:
    import page14