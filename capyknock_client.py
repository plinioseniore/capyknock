# capyknock client
#
#   The pyknock client request the server to open a specific port/ip
#   the request is formatted as JSON and use a symmetric encryption
#   for all the fields out of the username.
#   
#   The request include an OTP code that is generated externally on
#   apps like Google Authenticator or similar.
#   
#   WARNING : This implementation is not designed to prevent MITM
#             because the source IP address is not included in the
#             payload on purpose, to do not depend on an external
#             service like ipify or similar.
#             
#             The field "myip" is anyhow available and processed by
#             the server. So it can be extended to prevent MITM.
#
#   As the main goal of capyknock is to reduce noise in logs and
#   exploitation of zero days, it should not be used as the only
#   authentication method. Behind the port that gets open with the 
#   knock a strong authentication shall be set and possible a fail2ban.

import json
import socket
import time
from cryptography.fernet import Fernet

# Load configuration, available parameters will be:
#   {
#    "username"           : "",
#    "udpkey"             : "",
#    "otpkeydesc"		  : "",
#    "knock_server_ip"    : "",
#    "knock_server_port"  : "",
#    "target_server_ip"   : "",
#    "target_server_port" : ""
#   }
def loadconf():
    with open('capyknock_client-conf.json', 'r') as file:
        return json.load(file)

# Open a TCP connection and close it just after, just to verify if the port is open
def is_port_open(ip, port, timeout=2):
    try:
        with socket.create_connection((ip, port), timeout=timeout) as sock:
            sock.close()
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False

def nextauthentication(ip, port):
    # At this stage the next authentication can be run
    # there are two option, run from here the client
    # using subprocess or alternatively you can run
    # pyknock_client from a batch file and let the
    # batch to call the next client once pyknock_client
    # is terminated, an example for Windows:
    #
    # @echo off
    # title pyknock
    # cls
    # cd %cd%\pyknock_client
    # pyknock_client.exe
    # cd..
    # cd %cd%\ssh
    # start sshclient.exe	  
    # exit
    print("")

def waitingforthesun(s):        
    for _ in range(int(s)):
        time.sleep(1)
        print(f".", end="", flush=True)
    print("")

# Banner found somewhere on the net, not sure about copyright
banner=r"""
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣞⣆⢀⣠⢶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣀⡤⠤⠖⠒⠋⠉⣉⠉⠹⢫⠾⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⡏⢰⡴⠀⠀⠀⠉⠙⠟⠃⠀⠀⠀⠈⠙⠦⣄⡀⢀⣀⣠⡤⠤⠶⠒⠒⢿⠋⠈⠀⣒⡒⠲⠤⣄⡀⠀⠀⠀⠀⠀⠀
⢸⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠴⠂⣀⠀⠀⣴⡄⠉⢷⡄⠚⠀⢤⣒⠦⠉⠳⣄⡀⠀⠀⠀
⠸⡄⠼⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⡂⠠⣀⠐⠍⠂⠙⣆⠀⠀
⠀⠙⠦⢄⣀⣀⣀⣀⡀⠀⢷⠀⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⡇⠠⣀⠱⠘⣧⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠉⢷⣧⡄⢼⠀⢀⠀⠀⠀⠀⠀capyknock     ⠀ ⠈⠀⡈⠀⢄⢸⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⡀⠃⠘⠂⠲⡀⠀⠀⠀         ⠀⠀    ⠀ ⠙⠀⡈⢘⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢫⡑⠣⠰⠀⢁⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠁⣸⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣯⠂⡀⢨⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡆⣾⡄⠀⠀⠀⠀⣀⠐⠁⡴⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⡈⡀⢠⣧⣤⣀⣀⡀⢀⡀⠀⠀⢀⣼⣀⠉⡟⠀⢀⡀⠘⢓⣤⡞⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⡁⢁⣸⡏⠀⠀⠀⠀⠁⠀⠉⠉⠁⠹⡟⢢⢱⠀⢸⣷⠶⠻⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡏⠈⡟⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠁⠀⠻⣧⠀⠀⣹⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡤⠚⠃⣰⣥⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠼⢙⡷⡻⠀⡼⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠟⠿⡿⠕⠊⠉⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣾⠉⣹⣷⣟⣚⣁⡼⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

try:
    print(banner)
    
    # Load configuration parameters
    print(f"[*] Loading conf file...")
    conf = loadconf()
    
    # Init the chiper
    cipher = Fernet(conf['udpkey'].encode()) 
    
    
    while True:
        # If the port is not already open, ask for the OTP code
        if not is_port_open(conf['target_server_ip'], int(conf['target_server_port'])):
            otp_input = input(f"Enter the OTP code for {conf['otpkeydesc']}: ").strip()

            if not otp_input.isdigit():
                print("Only digits are allowed")
            elif otp_input == "":
                print("The OTP code cannot be blank")
            elif len(str(otp_input))!=6:
                print("The OTP code must have 6 digits")
            else:
                otp_value = otp_input
                
                # Only the payload is encoded so that at server side the username can be used to select the decryption key
                payload = {"otpcode"    : otp_value,                        # OTP Code
                           "trgsrvip"   : conf['target_server_ip'],         # Target Server IP
                           "trgsrvport" : conf['target_server_port'],       # Target Server Port
                           "myip"       : "",                               # Empty by default
                           "hash"       : ""                                # For future use
                          }
                json_payload = json.dumps(payload).encode()
                encrypted_payload = cipher.encrypt(json_payload)
                
                
                # Format as JSON
                data = {"usrnm"     : conf['username'],                      # Username
                        "payload"   : encrypted_payload.decode()             # Payload
                       }        
                json_payload = json.dumps(data).encode()
                
                # Send JSON via UDP
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                for _ in range(3):  # Repeat three times
                    sock.sendto(json_payload, (conf['knock_server_ip'], int(conf['knock_server_port'])))
                sock.close()

                # Print a state message and wait
                print(f"Request to open port {conf['target_server_port']} on server {conf['target_server_ip']} sent", end="", flush=True)
                waitingforthesun(5)
                
                # Verify if the port is open on the target server
                if is_port_open(conf['target_server_ip'], int(conf['target_server_port'])):
                    print(f"Port {conf['target_server_port']} is open on {conf['target_server_ip']}")
                    nextauthentication(conf['target_server_ip'], conf['target_server_port'])
                    print(f"This window will close automatically in few seconds", end="", flush=True)
                    waitingforthesun(3)
                    break
                else:
                    print(f"Failed to open port {conf['target_server_port']} on target {conf['target_server_ip']}. Retry or contact a system administrator.")
        else:
            print(f"Port {conf['target_server_port']} is open on {conf['target_server_ip']}")
            nextauthentication(conf['target_server_ip'], conf['target_server_port'])
            print(f"This window will close automatically in few seconds", end="", flush=True)
            waitingforthesun(3)
            break


except Exception as e:
            print(f"pyknock_client error message : {e}")
            waitingforthesun(30)