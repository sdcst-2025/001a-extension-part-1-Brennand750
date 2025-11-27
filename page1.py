from os import system
from rich import print
system("clear||cls")
print("Hello there!, Welcome to the first day at the wizard academy!")

print("This where you will learn all about the wonderous world of the wizard world!")

print("First. before you start, Please pick a class to become on your jouney")

print("[bold green] If you pick the potion class go to page 2 " 
      " [bold yellow] If you pick the wand class go to page 3 "
       " [bold blue] If you pick the beasts and monsters class go to page 4 ")
choice = input("Where will you want to go to next?")
if choice == "2":
 import page2
if choice == "3":
 import page3
else:
 import page4
 