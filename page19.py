from os import system
system ("clear || cls")
print('You go back to sleep for a little bit for the exam.')

print('Do you still want to go party page 18 or keep studying for the night page 20')
choice = input("Where would you like to go to next")
if choice == "18":
    import page18
else:
    import page20