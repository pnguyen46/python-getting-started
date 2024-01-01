# Installing packages
# Install an individual package
# - pip install colorama
# Install from a list of packages
# - pip install -r requirements.txt
#   - requirements.txt
#       - colorama

import colorama

colorama.init()
print(colorama.Fore.RED + 'This is red')

from colorama import *

init()
print(Fore.BLUE + 'This is blue')

from colorama import init, Fore
print(Fore.GREEN + 'This is green')
