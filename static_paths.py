'''Includes several functions to work with static ports.
   Enables you to get all static path bindings and their attributes,
   finds which EPGs the static path binding is bound to.

   This file is intended imported as a module and contains the following
functions:

    * get_all_static_path_objects(cookies): - gets all static path bindings and their attributes
    * find_static_path_binding_to_epgs -   finds which EPGs the static path binding is bound to'''

import requests
from credentials import APIC_HOST



def get_all_static_path_objects(cookies):

    '''Gets all static path objects and their attributes.'''

    uri = APIC_HOST + '/api/node/class/fvRsPathAtt.json'

    response = requests.get(uri , verify=False, cookies=cookies)

    return response

def get_all_static_path_t_dn_s(imdata):
    '''Finds list of static paths, removes duplicates.'''
    t_dn_list = []
    for static_path_object in imdata:
        t_dn = static_path_object['fvRsPathAtt']['attributes']['tDn']
        if t_dn not in t_dn_list:
            t_dn = static_path_object['fvRsPathAtt']['attributes']['tDn']
            t_dn_list += [t_dn]
    return t_dn_list


# Finds the DNs of EPGs in which the inputted static path is bound to.

def find_static_path_binding_to_epgs(imdata, static_path):
    '''Finds the DNs of EPGs in which the inputted static path is bound to.'''

    dn_list = []
    for static_path_object in imdata:
        t_dn = static_path_object['fvRsPathAtt']['attributes']['tDn']
        if t_dn == static_path:
            dn = static_path_object['fvRsPathAtt']['attributes']['dn']
            dn_list += [dn]
    return dn_list
