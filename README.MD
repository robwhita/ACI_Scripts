# Use Case
Had a customer who wanted to be able to quickly view and then delete static path bindings across several EPGs at the same time. 

For example, let's say you have a static path for leaf 101 interface 1/1. You then bind that static path across 50 EPGs. You could then use these scripts to see which 50 EPGs the static path leaf 101 interface 1/1 was bound to. Once you determine which EPGs the static path for leaf 101 interface 1/1 was bound to, you could then quickly delete the 50 static path bindings instead of manually deleting them one by one.


# Script Information

`find_static_path_to_epg_bindings.py`:

 This file is intended to be run as a script. When you run the script you will see all static paths, once you view all static paths, you then select one static path and the script will show you which EPGs that static path is bound to.

`delete_static_path_bindings.py`:

 Like the find_static_path_to_epg_bindings script, the delete_static_path_bindings script will show you which EPGs a static path is bound to. However, after the static path bindings are displayed, you will then be prompted to delete them. Use the delete_static_path_bindings script with extreme caution. 

`credentials.py` :

 You must enter in your credentials and the hostname or IP address of your APIC. 

`get_token.py`:

 Used as a module. Authenticates into the APIC and retrieves token.

`static_paths.py`:

 Used as a module. Includes several functions to work with static path bindings. Enables you to get all static path bindings and their attributes, finds which EPGs the static path binding is bound to.


# Disclaimer: Recommended to Run in a Test Environment First
You should run this in a test environment first. 

For the find_static_path_to_epg_bindings script, you can use the ACI Always-on sandbox to view static ports and their bindings. 

However, the ACI Always-on sandbox is shared amongst multiple people at the same time. Because you shouldn't delete other people's static path bindings, you shouldn't use the ACI Always-on sandbox. When deleting static path bindings, you can reserve an ACI APIC sandbox. 

https://devnetsandbox.cisco.com/RM/Topology 

Before deleting static path bindings in production make sure to backup your APIC's configuration. The author of this script is not responsible for any unexpected behavior after running the script.

# Using the find_static_path_to_epg_bindings.py script

1. Update the credentials.py file to include your APIC's credentials and hostname. 

2. Run the script. 

```bash
PS C:\ACI_Scripts> python find_static_path_to_epg_bindings.py

Below is a list of your static paths:

topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2B]
topology/pod-1/paths-101/pathep-[eth1/10]
topology/pod-1/protpaths-101-102/pathep-[SnV_FI-1A]
topology/pod-1/protpaths-101-102/pathep-[SnV_FI-1B]
```

3. Copy and paste one of the statics path above into the next part of the script. The script will show you the DNs of the EPGs to which the static path is bound to.

```bash
Please enter a static path from above to find out which EPGs it is bound to: topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2B]

****************************************************************************************************


Your static_path topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2B] is bound at the following EPGs:

uni/tn-Heroes/ap-Save_The_Planet/epg-app/rspathAtt-[topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2B]]
uni/tn-Heroes/ap-Save_The_Planet/epg-web/rspathAtt-[topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2B]]
uni/tn-Heroes/ap-Save_The_Planet/epg-db/rspathAtt-[topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2B]]
```

# Using the delete_static_path_bindings.py script

1. Update the credentials.py file to include your APIC's credentials and hostname. 

2. Run the script. 

```bash
PS C:\ACI_Scripts> python delete_static_path_bindings.py

Below is a list of your static paths:

topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2B]
topology/pod-1/paths-101/pathep-[eth1/10]
topology/pod-1/protpaths-101-102/pathep-[SnV_FI-1A]
topology/pod-1/protpaths-101-102/pathep-[SnV_FI-1B]


Press Enter to continue...
```

3. Copy and paste one of the statics path above into the next part of the script. The script will show you the DNs of the EPGs to which the static path is bound to.

```bash
Please enter a static path from above to find out which EPGs it is bound to: topology/pod-1/protpaths-101-102/pathep-[Heroes_FI
-2B]

****************************************************************************************************


Your static_path topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2B] is bound at the following EPGs:

uni/tn-Heroes/ap-Save_The_Planet/epg-app/rspathAtt-[topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2B]]
uni/tn-Heroes/ap-Save_The_Planet/epg-web/rspathAtt-[topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2B]]
uni/tn-Heroes/ap-Save_The_Planet/epg-db/rspathAtt-[topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2B]]


Press Enter to continue...
```

4. Finally, enter 'y' to delete the listed static path bindings. Enter 'n' to abort. You should receive a 200 status code for every static path binding that was deleted. 


```bash
****************************************************************************************************

uni/tn-Heroes/ap-Save_The_Planet/epg-app/rspathAtt-[topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2B]]
uni/tn-Heroes/ap-Save_The_Planet/epg-web/rspathAtt-[topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2B]]
uni/tn-Heroes/ap-Save_The_Planet/epg-db/rspathAtt-[topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2B]]


Would you like to delete the static path binding(s)in yellow above? Enter 'y' to delete the static path bindings. Enter 'n' to abort [y/n]: y
https://10.10.20.14/api/node/mo/uni/tn-Heroes/ap-Save_The_Planet/epg-app/rspathAtt-[topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2B]].json
200
https://10.10.20.14/api/node/mo/uni/tn-Heroes/ap-Save_The_Planet/epg-web/rspathAtt-[topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2B]].json
200
https://10.10.20.14/api/node/mo/uni/tn-Heroes/ap-Save_The_Planet/epg-db/rspathAtt-[topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2B]].json
200
```
