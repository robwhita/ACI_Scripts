
''' THe intent of the script is to get a list of all of your static path bindings.
 Once you receive a list of static path bindings
 you can then enter in a specific static path and see which EPGs it is bound to.
 This file is intended to be run as a script and import the following modules:

    * get_token - Enables you to authenticate into the APIC
      and receive a token for subsequent API calls.
    * static_paths -   Includes several functions to work with static ports.'''

import json
import requests
from colorama import init, Fore
import get_token
import static_paths

requests.packages.urllib3.disable_warnings() 

init(autoreset=True)

# Retrieves authentication token

token = get_token.get_token()

# Gets all static path objects and their attributes

all_static_path_objects = static_paths.get_all_static_path_objects(token)

all_static_path_objects_dict  = json.loads(all_static_path_objects.text)
imdata = all_static_path_objects_dict['imdata']

# Converts all static path objects and their attributes to a dictionary
# and retrieves data within 'imdata' key.

list_of_static_ports = static_paths.get_all_static_path_t_dn_s(imdata)

print((Fore.WHITE + '\nBelow is a list of your static paths:\n'))

for t_dn in list_of_static_ports:
    print(Fore.GREEN + t_dn)

# User enters in the static path binding

static_path = input(Fore.WHITE + '\nPlease enter a static path from above to find out which EPGs it is bound to: ')

print('\n' + '*' * 100 + '\n')

# Finds which DNs of EPGs the inputted static path is bound to.

dn_list = static_paths.find_static_path_binding_to_epgs(imdata, static_path)

# Prints string to user.

print(Fore.WHITE + (f'\nYour static_path {static_path} is bound at the following EPGs:\n'))

# For loop to print DNs of EPGs the inputted static path is bound to.

for dn in dn_list:
    print(Fore.GREEN + (dn))

print('')
