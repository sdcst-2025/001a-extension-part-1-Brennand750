from os import system
system ("clear || cls")
print('You rest for a couple of hours, and go to sleep. When you wake up a student tells you that the school is having a big dinner.')

print("But you also still feel tired from waking up and you have a exam tomorrow.")

print('What do you want to do?')

print('Do you want to go to the dinner page 18, or do you want go back to sleep, so you are ready for your exam. page 19.')
choice = input("Where would you like to go to next?")
if choice == "18":
    import page18
else:
    import page19