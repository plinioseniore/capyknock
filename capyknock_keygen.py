from cryptography.fernet import Fernet
import time
import json
import pyotp
import random
import string
import qrcode

chars = string.ascii_letters + string.digits

# Wait for s seconds and print dots
def waitingforthesun(s):        
    print(f"Closing in few seconds", end="", flush=True)
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

# Generate keys
udpkey      = Fernet.generate_key()
otpkey      = pyotp.random_base32()
username    = ''.join(random.choice(chars) for _ in range(24))

with open('capyknock_keygen-conf.json', 'r') as file:
    conf = json.load(file)

print(banner)
print("         Config and key generator")
print()
print()

print(f"username : " + str(username))
nickname = input(f"Inser user nickname for the username : ").strip()
print(f"udpkey : " + udpkey.decode())
print(f"otpkey : " + str(otpkey))
target_server_ip    = input(f'Inser target server IP {conf["target_server_ip"]}   : ').strip() or conf["target_server_ip"]
target_server_port  = input(f'Inser target server port {conf["target_server_port"]} : ').strip() or conf["target_server_port"]
knock_server_port  = input(f'Inser target knock port {conf["knock_server_port"]} : ').strip() or conf["knock_server_port"]

uri = pyotp.totp.TOTP(otpkey).provisioning_uri(
    name=f'{nickname}@IT2C',
    issuer_name=f'IT2C Remote Conns')

qrcode.make(uri).save(f"qr_{nickname}_{str(username)}.png")

print()
print("### Server Config ###")
print(f'      "username"              : "{str(username)}",')
print(f'      "nickname"              : "{str(nickname)}",')
print(f'      "udpkey"                : "{udpkey.decode()}",')
print(f'      "otpkey"                : "{str(otpkey)}",')
print(f'      "target_server_ip"      : "{str(target_server_ip)}",')
print(f'      "target_server_port"    : "{str(target_server_port)}"')

print()
print("### Client Config ###")
print(f'      "username"              : "{str(username)}",')
print(f'      "udpkey"                : "{udpkey.decode()}",')
print(f'      "otpkeydesc"            : "{str(nickname)}@IT2C",')
print(f'      "knock_server_ip"       : "{str(target_server_ip)}",')
print(f'      "knock_server_port"     : "{str(knock_server_port)}",')
print(f'      "target_server_ip"      : "{str(target_server_ip)}",')
print(f'      "target_server_port"    : "{str(target_server_port)}"')

print()
print("### Client Config (M2M) ###")
print(f'      "username"              : "{str(username)}",')
print(f'      "udpkey"                : "{udpkey.decode()}",')
print(f'      "otpkey"                : "{str(otpkey)}",')
print(f'      "knock_server_ip"       : "{str(target_server_ip)}",')
print(f'      "knock_server_port"     : "{str(knock_server_port)}",')
print(f'      "target_server_ip"      : "{str(target_server_ip)}",')
print(f'      "target_server_port"    : "{str(target_server_port)}"')
print()

waitingforthesun(60)