### Manipulate Windows Firewall ###
#
#   Example usage
#       >>> add_firewall_rule("_capyknock","1.1.1.1","8888")
#       Name                          : {413c19aa-5867-4a27-a887-68dcc77cc8e9}
#       DisplayName                   : _capyknock
#       ...
#       

#       >>> add_firewall_rule("_capyknock","2.2.2.2","8888")
#       Name                          : {267a7ba4-e1b9-4f6d-9c78-7d28121852fc}
#       DisplayName                   : _capyknock
#       ...
#       
#       Firewall rule '_capyknock' added successfully.
#       >>> firewall_rule_exists("DisplayName", "_capyknock")
#       True
#       >>> firewall_list_rules("*capy*")
#       ['_capyknock']
#       >>> firewall_list_ips("DisplayName", "_capyknock")
#       ['2.2.2.2', '1.1.1.1']
#       >>> firewall_rule_delete("DisplayName", "_capyknock")
#       True
#       >>> firewall_list_ips("DisplayName", "_capyknock")
#       ['']
#       >>> firewall_rule_exists("DisplayName", "_capyknock")
#       False
#       >>>
#       >>> firewall_delete_by_ip("*capy*","1.1.1.1")
#       True
#       
import subprocess
from datetime import datetime, timedelta
from collections import deque

# Create a new firewall rule
#  
#  The rule_name is the DisplayName that shall not be unique
#  if multiple rules with same DisplayName are created they
#  can be managed all together by DisplayName
def add_firewall_rule(rule_name, ip_address, port):
    command = [
        "powershell",
        "-Command",
        f"New-NetFirewallRule -DisplayName '{rule_name}' -Direction Inbound -Action Allow "
        f"-RemoteAddress {ip_address} -Protocol TCP -LocalPort {port}"
    ]
    try:
        subprocess.run(command, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def firewall_rule_exists(rule_property, rule_name):
    command = [
        "powershell",
        "-Command",
        f"Get-NetFirewallRule -{rule_property} '{rule_name}'"
    ]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        if result.stdout.strip():
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False

# Return a list object with all the firewall rules that match the search_pattern
def firewall_list_rules(search_pattern):
    command = [
        "powershell",
        "-Command",
        f"Get-NetFirewallRule -DisplayName '{search_pattern}' | Select DisplayName"
    ]
    try:
        # Get the stdout of the command
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        # Manipulate the string to get a comma separated list
        result = result.stdout.strip("\n").replace("\n\n\n","").replace("\n",",").replace(" ","")
        # Move from a comma separated string to a list and skip the first two results
        result = result.split(",")
        result = result[2:]
        result = list(set(result))
        if result:
            return result
        else:
            return
    except subprocess.CalledProcessError:
        return

# Return a list object with all the current TCP connection to tcpport
def listcurrentconnection():
    command = [
        "powershell",
        "-Command",
        f"Get-NetTCPConnection -State Established | Select RemoteAddress"
    ]
    try:
        # Get the stdout of the command
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        # Manipulate the string to get a comma separated list
        result = result.stdout.strip("\n").replace("\n\n\n","").replace("\n",",").replace(" ","")
        # Move from a comma separated string to a list and skip the first two results
        result = result.split(",")
        result = result[2:]
        result = list(set(result))
        if result:
            return result
        else:
            return
    except subprocess.CalledProcessError:
        return    


# Search rules by pattern on Name (unique value autoassigned at rule creation)
def firewall_list_rules_ids(search_pattern):
    command = [
        "powershell",
        "-Command",
        f"Get-NetFirewallRule -DisplayName '{search_pattern}' | Select Name"
    ]
    try:
        # Get the stdout of the command
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        # Manipulate the string to get a comma separated list
        result = result.stdout.strip("\n").replace("\n\n\n","").replace("\n",",").replace(" ","")
        # Move from a comma separated string to a list and skip the first two results
        result = result.split(",")
        result = result[2:]
        result = list(set(result))
        if result:
            return result
        else:
            return
    except subprocess.CalledProcessError:
        return

# Delete the firewall rule
def firewall_rule_delete(rule_property, rule_name):
    command = [
        "powershell",
        "-Command",
        f"Remove-NetFirewallRule -{rule_property} '{rule_name}'"
    ]
    try:
        if(firewall_rule_exists(rule_property, rule_name)):
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False

# List the ip address in a firewall rule
def firewall_list_ips(rule_property, rule_name):
    # Get current remote addresses
    get_cmd = [
        "powershell",
        "-Command",
        f"(Get-NetFirewallRule -{rule_property} '{rule_name}' | "
        f"Get-NetFirewallAddressFilter).RemoteAddress"
    ]
    try:
        result = subprocess.run(get_cmd, capture_output=True, text=True, check=True)
        current_ips = result.stdout.strip().split("\n")
        return current_ips
    except subprocess.CalledProcessError:
        return

# Loop all rules that match the search_pattern and delete the rule if contains
# a match with ip_address
def firewall_delete_by_ip(search_pattern, ip_address):
    rules = firewall_list_rules_ids(search_pattern)
    
    for rule in rules:
        ips = firewall_list_ips("Name", rule)
        if ip_address in ips:
            return firewall_rule_delete("Name", rule)
        
    

# Helper functions
rule_prefix = "_capyknock_"
allowedip_queue  = deque(maxlen=100)

def ndays():
    today = datetime.today()
    ref = datetime(2025, 1, 1)
    return (today - ref).days

def load_firewall_ip():
    global allowedip_queue
    ips = firewall_list_ips("DisplayName", str(rule_prefix) + "*")
    
    # We used the firewall IPs contained in the rules as master data
    # so here we clear all IPs in the allowedip_queue and reload 
    # from the firewall rules
    allowedip_queue.clear()
    for ip in ips:
        allowedip_queue.append(ip)
    

def cleanup_firewall():
    # Get names of current rules
    global rule_prefix
    rules = firewall_list_rules(rule_prefix+"*")
    # Get IPs currently connected
    connectedips = listcurrentconnection()
    # Number of days from a common reference is used to identify age of the rule
    nday = ndays()

    if(rules):
        for rule in rules:
            refdate = int(rule.replace(rule_prefix,"")) # Example _capyknock_300 -> 300
            if((nday-refdate)>2):                       # Rule is older than 2 days
                
                # Get rule IDs (referred as Name in Windows Firewall)
                ruleids = firewall_list_rules_ids(rule)
                for ruleid in ruleids:
                    # We want to delete the rule only if the IP address contained in it are not currently connected
                    ips = firewall_list_ips("Name", ruleid)
                    for ip in ips:                                      # Loop the firewall rule IPs
                        if ip not in connectedips:                      # If the connected IPs are not in the firewall rule IPs, we can delete the rule
                            firewall_rule_delete("Name", ruleid)
                            
                        
                   
               
 
   

def action_allow_ip(ip_address, port):
    global allowedip_queue
    global rule_prefix
    
    # Add the IP address in the local queue (RAM only)
    if ip_address not in allowedip_queue:
        if(add_firewall_rule(str(rule_prefix) + str(ndays()), ip_address, port)):
            allowedip_queue.append(ip_address)
            return True
    return False   

def action_block_ip(ip_address):
    global rule_prefix
    return firewall_delete_by_ip(rule_prefix+"*", ip_address)
    

