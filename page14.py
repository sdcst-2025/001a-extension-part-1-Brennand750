from os import system
system ("clear || cls")
print("When you ask a student about the situation some of them didn't what to do except for two people Bob and Liam")

print('Which person do you ask for help?')

print('If you ask Bob go to page 17')

print('If you ask Liam go to page 15')
choice = input("Where would you like to go to next?")
if choice == "17":
    import page17
else:
    import page15