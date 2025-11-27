from os import system
from rich import print
system ("clear || cls")
print("[bold yellow] In today's lesson you are going to learn the Stupefy spell using your wand.")

print("[bold yellow] When you used this spell, you stunned a student")

print('[bold yellow] Will you go to the head master for help? page 13')

print('[bold yellow] Or will you ask a student for help? page 14')
choice = input("Where would you like to go to next?")
if choice == "13":
    import page13
else:
    import page14