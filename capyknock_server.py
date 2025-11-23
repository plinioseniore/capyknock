banner=r"""
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣞⣆⢀⣠⢶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣀⡤⠤⠖⠒⠋⠉⣉⠉⠹⢫⠾⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⡏⢰⡴⠀⠀⠀⠉⠙⠟⠃⠀⠀⠀⠈⠙⠦⣄⡀⢀⣀⣠⡤⠤⠶⠒⠒⢿⠋⠈⠀⣒⡒⠲⠤⣄⡀⠀⠀⠀⠀⠀⠀
⢸⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠴⠂⣀⠀⠀⣴⡄⠉⢷⡄⠚⠀⢤⣒⠦⠉⠳⣄⡀⠀⠀⠀
⠸⡄⠼⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⡂⠠⣀⠐⠍⠂⠙⣆⠀⠀
⠀⠙⠦⢄⣀⣀⣀⣀⡀⠀⢷⠀⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⡇⠠⣀⠱⠘⣧⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠉⢷⣧⡄⢼⠀⢀  capyknock-server ⠀ ⠈⠀⡈⠀⢄⢸⡄
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

print(banner)
print("[*] Importing modules...")

from scapy.all import AsyncSniffer, IP, UDP, conf
from cryptography.fernet import Fernet
from collections import deque
from datetime import datetime
import json
import socket
import time
import pyotp
import logging
from logging.handlers import TimedRotatingFileHandler
from capyknock_winfirewall import *

# Global Variables
incoming_IP             = ""
incoming_JSON           = ""
incoming_IP_queue       = deque(maxlen=10)
incoming_JSON_queue     = deque(maxlen=10)
current_time            = ""
otp_queue               = deque(maxlen=100)
bannedip_queue          = deque(maxlen=100)
banning_IP              = ""

# Configure logging to write to a file
def setup_logger():
    # Create a logger
    logger = logging.getLogger("daily_logger")
    logger.setLevel(logging.INFO)

    # Create a handler that rotates daily
    handler = TimedRotatingFileHandler(
        "capyknock.log",    # Log file name
        when="midnight",    # Rotate at midnight
        interval=1,         # Every 1 day
        backupCount=15      # Keep that number of files
    )
    
    # Set log format
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)

    # Add handler to logger
    logger.addHandler(handler)
    return logger



# Custom logging
def printlog(message):
    print(message)                # Print to console
    logging.info(message)         # Log to file


# Load configuration, available parameters will be:
#       {
#         "users": 
#         [
#           {
#             "username"     		: "",
#       	  "nickname"     		: "",
#       	  "udpkey"       		: "",
#       	  "otpkey"       		: "",
#       	  "target_server_ip"	: "",
#       	  "target_server_port"	: ""
#           }
#         ]
#       }
def loadconf():
    with open('capyknock_server-conf.json', 'r') as file:
        return json.load(file)

# Wait for s seconds and print dots
def waitingforthesun(s):        
    print(f"Closing in few seconds", end="", flush=True)
    for _ in range(int(s)):
        time.sleep(1)
        print(f".", end="", flush=True)
    print("")

# Loop the nested JSON from the configuration file
# and return the user.
#
# Example:
#    user = get_user(user_conf, "QMQsrABBpkzunySvkzmizCw1")
#    if(user):
#        printlog(f"username: {user['username']}")
#        printlog(f"nickname: {user['nickname']}")
#        printlog(f"udpkey: {user['udpkey']}")
#        printlog(f"otpkey: {user['otpkey']}")
#        printlog(f"target_server_ip: {user['target_server_ip']}")
#        printlog(f"target_server_port: {user['target_server_port']}")
#
def get_user(user_conf, usr):
    for user in user_conf['users']:
        if(str(user['username'])==str(usr)):
            return user
    return

# Handle the packet and return IP and payload in JSON
def handle_packet(packet):
    global incoming_IP_queue
    global incoming_JSON_queue
    global bannedip_queue
    global banning_IP
    
    if packet.haslayer('UDP'):
        udp_payload = bytes(packet[UDP].payload)
        
        try:
            # Is expected a JSON payload in the UDP
            json_message = json.loads(udp_payload)
            
            # If the banip keyword is used
            if "banip" in json_message:
                # Process only request from localhost interface, to avoid that a remote user can abuse of the ban feature
                if(packet[IP].src == "127.0.0.1"):
                    banning_IP = json_message['banip']
                    printlog(f" > Received banning request for IP address : {json_message['banip']}")
            # If the usrnm keyword is used            
            elif "usrnm" in json_message:
                printlog(f" > Received UDP message from username : {json_message['usrnm']} from IP {packet[IP].src}")
                # Add incoming IP and JSON in the queue
                if(packet[IP].src not in incoming_IP_queue):
                    incoming_IP_queue.append(packet[IP].src)
                if(json_message not in incoming_JSON_queue):
                    incoming_JSON_queue.append(json_message)
            else:
                json_message = ""
            
        except Exception as e:
            printlog(f"Failed to decrypt or parse message: {e}")

##### Main #####
          
try:
    global allowedip_queue
    
    # Set current time and start logging
    current_time = time.time()
    logging = setup_logger()
    
    # Load configuration parameters
    printlog(f"[*] Loading conf file...")
    user_conf = loadconf()
    
    # Cleanup and load firewall
    printlog(f"[*] Cleanup firewall...")
    cleanup_firewall()
    printlog(f"[*] Loading firewall...")
    load_firewall_ip()
    
    printlog(f"[*] Available interfaces...")
    for i, iface in enumerate(conf.ifaces.values()):
        printlog(f"      if{i}: {iface.name}")
    
    # Choose the interface number you want (e.g., 1)
    iface_number1 = int(user_conf['listeninginterface'])
    iface_number2 = int(user_conf['locallisteninginterface'])
    iface_name = [str(list(conf.ifaces.values())[iface_number1].name), str(list(conf.ifaces.values())[iface_number2].name)]
    printlog(f"[*] Sniffer started on interface : {iface_name}")
    
    # Create an AsyncSniffer instance
    sniffer = AsyncSniffer(iface=iface_name, filter="udp dst port "+str(user_conf['listeningport']), prn=handle_packet, store=False)
    printlog(f"[*] Looking for UDP packets on port {str(user_conf['listeningport'])}")
    
    # Start sniffing in the background
    sniffer.start()
    
    ##### Loop #####
    try:    
        while True:
                ##############################################################
                # These global variables are written by the handle_packet
                if(banning_IP):
                    printlog(f" >> Processing ban of ip address : {banning_IP}")
                    if banning_IP in allowedip_queue:
                        printlog(f" >>> IP address : {banning_IP} found in the queue. Banned.")
                        bannedip_queue.append(banning_IP)
                        action_block_ip(banning_IP)
                    banning_IP = ""
                elif(incoming_IP_queue and incoming_JSON_queue):
                    
                    incoming_IP   = incoming_IP_queue.popleft()
                    incoming_JSON = incoming_JSON_queue.popleft()
                    
                    # Look for the user
                    user = get_user(user_conf, incoming_JSON['usrnm'])
                    if(user):
                        printlog(f" >> Found user : {user['username']} / {user['nickname']}")
                        
                        # Get keys for the identified user
                        cipher = Fernet(user['udpkey'].encode())
                        totp = pyotp.TOTP(user['otpkey'].encode())
                        
                        # Decrypt payload
                        try:
                            decrypt_payload = cipher.decrypt(incoming_JSON['payload'].encode())
                            decrypt_payload = decrypt_payload.decode()
                            printlog(f" >>> Decrypted payload : {decrypt_payload}")
                            json_payload = json.loads(decrypt_payload)
                        
                            # Get OTP code
                            otp_input = str(json_payload['otpcode']).strip()
                            if not otp_input.isdigit():
                                printlog(" >>>> Only digits are allowed")
                            elif otp_input == "":
                                printlog(" >>>> The OTP code cannot be blank")
                            elif len(str(otp_input))!=6:
                                printlog(" >>>> The OTP code must have 6 digits")
                            else:
                                printlog(f" >>>> Format of OTP code is valid")
                                otp_value = int(otp_input)
                                if(totp.verify(otp_value)):
                                    ##############################################################
                                    # Process here firewall manipulation, the following parameters
                                    # are available.
                                    #
                                    #   incoming_IP
                                    #   otp_value
                                    #   json_payload['trgsrvip']
                                    #   json_payload['trgsrvport']
                                    #   json_payload['myip']
                                    #   json_payload['hash']
                                    #   user['target_server_ip']
                                    #   user['target_server_port']
                                    
                                    # Verify that the OTP code has not already being processed
                                    if otp_value not in otp_queue:
                                        printlog(f" >>>>> Authentication succesfull, OTP code is valid.")        
                                        otp_queue.append(otp_value)
                                        
                                        # Verify that the IP address is not in the list of banned ones
                                        if incoming_IP not in bannedip_queue:
                                            printlog(f" >>>>>> The IP address is not banned")
                                            # Verify that target server match the allowed one in the server configuration
                                            if(json_payload['trgsrvip'] == user['target_server_ip']):
                                                printlog(f" >>>>>> Target server IP address match")
                                                # Verify that target port match the allowed one in the server configuration
                                                if(json_payload['trgsrvport'] == user['target_server_port']):
                                                    printlog(f" >>>>>> Target server IP port match")
                                                    # At this stage we can manipulate the firewall
                                                    if(json_payload['myip'] != ""):
                                                        printlog(f" >>>>>>> Open firewall rule for IP address in the JSON")
                                                        if(action_allow_ip(json_payload['myip'], user['target_server_port'])):
                                                            printlog(f" >>>>>>> The IP address has been included in the allow list")
                                                        else:
                                                            printlog(f" >>>>>>> The IP address is already included in the allow list or has not been added in the firewall.")
                                                    else:
                                                        printlog(f" >>>>>>> Open firewall rule for IP address in the IP packet")
                                                        if(action_allow_ip(incoming_IP, user['target_server_port'])):
                                                            printlog(f" >>>>>>> The IP address has been included in the allow list")
                                                        else:
                                                            printlog(f" >>>>>>> The IP address is already included in the allow list or has not been added in the firewall.")
                                                
                                    else:
                                        printlog(f" >>>>> Authentication failed, OTP code already used.")
    
                                else:
                                    printlog(f" >>>>> Authentication failed, OTP code is invalid.")
                                    
                        except Exception as e:
                            printlog(f" >>> Failed to decrypt message {e}") 
                    else:
                        printlog(f" >> Not found user : {incoming_JSON['usrnm']}")
                    

                    # Once processed, reset values
                    incoming_IP = ""
                    incoming_JSON = ""
                    
                ##############################################################
                # Once every 12 hours
                if((time.time()-current_time)>(12*60*60)):
                    cleanup_firewall()
                    load_firewall_ip()
                    printlog(f" > Periodical cleanup and reload the firewall")
                    current_time = time.time()
                pass
                
                # Poor's man approach to don't burn the CPU
                time.sleep(1)
            
    except KeyboardInterrupt:
        sniffer.stop() 
        printlog("Stopping sniffer.")
        waitingforthesun(30)
                       
    except Exception as e:
       sniffer.stop()         
       printlog(f"Error message : {e}")
       waitingforthesun(30)
    

except Exception as e:
            printlog(f"Error message : {e}")
            waitingforthesun(30)