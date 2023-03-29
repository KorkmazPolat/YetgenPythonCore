import os
import time

# Define colors
GREEN = '\033[32m'
DARK = '\033[40m'

# Clear the screen
os.system('clear')

# Print the hacker screen
print(DARK)
print("Loading...")
time.sleep(2)
print(GREEN + """
               ██████╗ ██╗  ██╗███████╗███████╗
              ██╔═══██╗██║ ██╔╝██╔════╝██╔════╝
              ██║   ██║█████╔╝ █████╗  █████╗  
              ██║   ██║██╔═██╗ ██╔══╝  ██╔══╝  
              ╚██████╔╝██║  ██╗███████╗███████╗
               ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝
    
    Welcome to the hacker screen!
    
""" + DARK)