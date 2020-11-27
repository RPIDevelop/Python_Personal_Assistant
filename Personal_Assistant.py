#!/usr/bin/python
import time
import os
import subprocess
from random import *
needed = True
path = ''
need = ""
#List of things user can do
items = ["CODE", "INTERNET", "FILES", "TIME"]
#Generate a greeting
greeting = choice(["Welcome back", "Hello", "Good to see you"])
#Greet the user
print(greeting,"Master")
time.sleep(0.7)
#Respond to their need
while needed == True:
    while need not in items:
        #Ask user what they need
        need = input("What would you like to do?").upper()
    if need == "CODE":
        print("Ok, I will open up the code editor")
        path = "geany"
        subprocess.call(path)
    elif need == "INTERNET":
        print("Ok, I will open the internet browser")
        path = "chromium-browser"
        subprocess.call(path)
    elif need == "TIME":
        print("This is the time:")
        print(time.strftime("%H:%M:%S"))
    elif need == "FILES":
        print("Ok, I will open the file browser")
        path = "pcmanfm"
        subprocess.call(path)
    else:
        pass
    user = input("Can I still be of assistance?").upper()
    if user == "NO":
        needed = False
    else:
        need = ""
        pass

farewell = choice(["Farewell", "Goodbye", "Se you soon"])
print(farewell,"Master")


    
    
