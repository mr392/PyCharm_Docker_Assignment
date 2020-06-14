import sys

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format

cprint(figlet_format('Hello! ', font='banner'),
       'red', 'on_yellow')

cprint(figlet_format('This works!', font='banner'),
       'red', 'on_yellow')