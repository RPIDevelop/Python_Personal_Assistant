# Python_Personal_Assistant
Here is a simple python personal assistant I coded in python!

DISCLAIMER:
The assistant was made to run on a Raspberry Pi with the latest version of Raspberry Pi OS installed

Modules Required to Run:
time,
os,
subprocess,
random


HOW TO USE

After saying hello, the assistant will ask you what you want to do.
You can either:
Open the code editor (Type CODE)
Open the internet browser (Type INTERNET)
Open the file browser (Type FILES)
Show the current time (Type TIME)
Open the terminal (Type TERMINAL)
Open the media browser (Type MEDIA)
Change file paths (Type CONFIG):
  After entering CONFIG, the assistant will ask you what you want to config, type in one of the above (Excluding TIME), 
  it will then ask you the file path. Enter in the file path, type yes when prompted, then test it! If it doesn't work,
  right-click on the application that wont open, press properties, then remember the first part of the file's name (The     part before the ".". Type that into the config prompt and it should work.

After you tell the assistant what to do, and after you are done using one of the listed items, the assistant will ask
you if it can do something else for you. Either respond with YES or NO. If you responded YES, the assistant will ask you
what you want to do again. If NO then it will say goodbye and the program will stop running.

If you use a Mac or Windows computer, please download the python file and make sure you have the required modules and apps.
I am currently working on a compiled Windows and Mac version.

NOTICE:
As far as I'm aware, for the CODE, INTERNET, TERMINAL, MEDIA, AND FILES to work, you will need to have the default Raspberry Pi applications. But feel free to change the path locations if you want the assistant to open something else.


