#!/usr/bin/env python

# Learned this code from StationX's course on python for ethical hacking 

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser() # Create parse object for command line tool
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_MAC", help="New MAC address")
    (options, arguments) = parser.parse_args() # save user inputs
    if not options.interface: # check the user input a interface
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_MAC: # check the user input a MAC address
        parser.error("[-] Please specify a new MAC, use --help for more info.")
    return options

def change_mac(interface, new_MAC):
    print("[+] Changing MAC address for " + interface + " to " + new_MAC)
    subprocess.call(["ifconfig", interface, "down"]) # cmd turn of interface
    subprocess.call(["ifconfig", interface, "hw", "ether", new_MAC]) # cmd change mac
    subprocess.call(["ifconfig", interface, "up"]) # cmd turn interface back on

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(['ifconfig', interface]) # run ifconfig [interface]
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result)) # search ^ output for mac addy
    if mac_address_search_result: # check that a mac was found
        return mac_address_search_result.group(0) # index for first result
    else:
        print("[-] Could not read mac address.")

options = get_arguments() # run function and get interface n MAC address
current_mac = get_current_mac(options.interface) # insert ^ interface into get mac func
print("Current MAC = " + str(current_mac))
change_mac(options.interface, options.new_MAC) # change mac adress

current_mac = get_current_mac(options.interface)
if current_mac == options.new_MAC: # determine if succesfull
    print("[+] MAC address was successfully changed to " + current_mac)
else:
    print("[-] MAC address did not get change.")
