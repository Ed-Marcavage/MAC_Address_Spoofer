# MAC_Address_Spoofer
Uses the Subprocess, Optparse, and Re modules in python to spoof a MAC address in a Linux OS 

Full credit to StationX for the [tutorial](https://courses.stationx.net/p/the-complete-python-for-hacking-and-cyber-security-bundle) that taught me this code 

# subprocess
## Use this module to create a python object that accepts user input and runs it in the linux terminal 
## Power down the target interface, then insert the new MAC address given by the user, and then power the interface back up 

# Re
## Use Pythons RegEx module to locate the changed mac address
## Compare the changed MAC address with the current, to insure it has successfully been altered 

# Optparse
## Use this module to create a python object that creates a linux command and saves user input
## Create a help menu for confused users 



