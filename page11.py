from os import system
from rich import print
system ("clear || cls")
print("[bold yellow] In today's lesson you are going to learn the episkey spell with your wand ")

print('[bold yellow] When you used the episkey spell it back fired and you hurt yourself.')

print('[bold yellow] Do you go to the headmaster for help? page 13')

print('[bold yellow] Or do you ask a student for help? page 14')
choice = input("Where would you like to go to next?")
if choice == "13":
    import page13
else:
    import page14