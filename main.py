
''' THe intent of the script is to get a list of all of your static path bindings.
 Once you recieve a list of static path bindings
 you can then enter in a specfic static path and see which EPGs it is bound to.
 This file is intended to be run as a script and importes the following modules:

    * get_token - Enables you to authenticate into the APIC
      and recieve a token for subsequent API calls.
    * static_paths -   Includes several functions to work with static ports.'''

import json
import get_token
import static_paths

# Retrieves authentication token

token = get_token.get_token()

# Gets all static path objects and their attributes

all_static_path_objects = static_paths.get_all_static_path_objects(token)

all_static_path_objects_dict  = json.loads(all_static_path_objects.text)
imdata = all_static_path_objects_dict['imdata']

# Converts all static path objects and their attributes to a dictionary
# and retrieves data within 'imdata' key.

list_of_static_ports = static_paths.get_all_static_path_t_dn_s(imdata)

print((f'Below is a list of your static paths:\n'))

for t_dn in list_of_static_ports:
    print(t_dn)

# User enters in the static path binding

static_path = input('\nPlease enter a static path from above to find out which EPGs they are bound to: ')


# Finds which DNs of EPGs the inputted static path is bound to.

dn_list = static_paths.find_static_path_binding_to_epgs(imdata, static_path)

# Prints string to user.

print((f'\nYour static_path {static_path} is bound at the following EPGs:\n'))

# For loop to print DNs of EPGs the inputted static path is bound to.

for dn in dn_list:
    print(dn)
