import json
import socket
import sys

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
    with open('capyknock_server-conf.json', 'r') as file:
        return json.load(file)

try:

    if len(sys.argv) > 1:
        print("Sending request to ban", sys.argv[1])
        
        # Load configuration parameters
        conf = loadconf()
        
        # Format as JSON
        data = {"banip"     : sys.argv[1]
            }        
        json_payload = json.dumps(data).encode()
        
        # Send JSON via UDP
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        for _ in range(3):  # Repeat three times
            sock.sendto(json_payload, ("127.0.0.1", int(conf['listeningport'])))
        sock.close()        
    else:
        print("No arguments provided")
        print("Usage to ban 192.168.1.1 : python capyknock_banip.py 192.168.1.1")
    
except Exception as e:
            print(f"Error message : {e}")