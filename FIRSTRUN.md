# Getting Started

This is a step by step guide to get capyknock running

## Generate Keys

Edit the `capyknock_keygen-conf.json` file and insert the following
- knock_server_port  : Is the UDP port that will be used by capyknock to sniff the packets for authentication
- target_server_ip   : The IP address on which capyknock will run, is assumed that is the same IP address on which the hidden service behind (like SSH) capyknock will run either 
- target_server_port : The port on which the hidden service (like SSH) will run
- issuer			 : The name of the issuer of the QR Code, information field only	

```
{
 "knock_server_port"  : "45091",	
 "target_server_ip"   : "127.0.0.1",
 "target_server_port" : "22",
 "issuer"			  : "plinio"
}
```

Save the file and run `capyknock_keygen.py`, you will get on the screen something like the below. Don't reuse the `udpkey` and `otpkey` listed below but use the one generated on your machine and keep them secret. Copy paste the output of the `capyknock_keygen.py` in a notepad application, it will remain on the screen for 30 seconds.

```
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

         Config and key generator


username : o73Z2SHNs029eUZxosVBFw51
Inser user nickname for the username : plinio
udpkey : F9DprZJS0CJcmSRVHPFa_vc9nJzD3Rkc8USoNQO2J7o=
otpkey : SMHH6ZJ4AEHNNWIZLPTJKZH54RKLHKRE
Inser target server IP 127.0.0.1   :
Inser target server port 22 :
Inser target knock port 45091 :
Inser issuer name  : myserver

### Server Config ###
      "username"              : "o73Z2SHNs029eUZxosVBFw51",
      "nickname"              : "plinio",
      "udpkey"                : "F9DprZJS0CJcmSRVHPFa_vc9nJzD3Rkc8USoNQO2J7o=",
      "otpkey"                : "SMHH6ZJ4AEHNNWIZLPTJKZH54RKLHKRE",
      "target_server_ip"      : "127.0.0.1",
      "target_server_port"    : "22"

### Client Config ###
      "username"              : "o73Z2SHNs029eUZxosVBFw51",
      "udpkey"                : "F9DprZJS0CJcmSRVHPFa_vc9nJzD3Rkc8USoNQO2J7o=",
      "otpkeydesc"            : "plinio@myserver",
      "knock_server_ip"       : "127.0.0.1",
      "knock_server_port"     : "45091",
      "target_server_ip"      : "127.0.0.1",
      "target_server_port"    : "22"

### Client Config (M2M) ###
      "username"              : "o73Z2SHNs029eUZxosVBFw51",
      "udpkey"                : "F9DprZJS0CJcmSRVHPFa_vc9nJzD3Rkc8USoNQO2J7o=",
      "otpkey"                : "SMHH6ZJ4AEHNNWIZLPTJKZH54RKLHKRE",
      "knock_server_ip"       : "127.0.0.1",
      "knock_server_port"     : "45091",
      "target_server_ip"      : "127.0.0.1",
      "target_server_port"    : "22"

### Secrets for symmetric share ###
Once used, destroy those keys. Do not save.
7zip psw : HMIVKWJTEVGXZ62DML3OEWDE7V3DXW2H
SSH psw  : HYJGP6LGFWNXEDM6G47BGSZVXXB4LGR5
OTP key  : SMHH6ZJ4AEHNNWIZLPTJKZH54RKLHKRE

Closing in few seconds...
```

The last three strings are 32 chars password/keys that you can use to:
- Share the client and the relevant secrets via 7zip, with encryption of the zipped file
- Have a first time use password (for SSH or any other service), that user will change later on
- Repetition of the OTP key, if you want the user to generate the QR code at their end using capyknock_qrcode.py

You will also get a QR Code as image, in this case the file is named `qr_plinio_o73Z2SHNs029eUZxosVBFw51.png`. Open any TOTP application (like Google Authenticator) and scan the QR Code.

## Configure the Server

Run `capyknock_server.py`, you will get something like the below with your network interfaces listed

```
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

[*] Importing modules...
[*] Loading conf file...
[*] Cleanup firewall...
[*] Loading firewall...
[*] Available interfaces...
      if0: Local Area Connection* 8
      if1: Local Area Connection* 7
      if2: Local Area Connection* 6
      if3: Bluetooth Network Connection 8
      if4: Local Area Connection* 10
      if5: Local Area Connection* 9
      if6: Ethernet 3
      if7: Wi-Fi
      if8: Loopback Adapter
      if9: VPN - VPN Client
      if10: VPN2 - VPN Client
      if11: Ethernet
[*] Sniffer started on interface : ['Local Area Connection* 8', 'Local Area Connection* 8']
[*] Looking for UDP packets on port 0
```

We want to run the server on interface 7 (Wi-Fi) and 8 (Loopback Adapter). The loopback is used for communication with `capyknock_banip.py`.

Edit `capyknock_server-conf.json` and insert the configuraiton generated and the interface details. The `listeningport` should match the `knock_server_port` in `capyknock_keygen-conf.json`.

```
{
  "listeninginterface": 7,
  "locallisteninginterface": 8,
  "listeningport": 45091,
  "users": 
  [
    {
      "username"              : "o73Z2SHNs029eUZxosVBFw51",
      "nickname"              : "plinio",
      "udpkey"                : "F9DprZJS0CJcmSRVHPFa_vc9nJzD3Rkc8USoNQO2J7o=",
      "otpkey"                : "SMHH6ZJ4AEHNNWIZLPTJKZH54RKLHKRE",
      "target_server_ip"      : "127.0.0.1",
      "target_server_port"    : "22"
    },
    {
      "username"              : "",
      "nickname"              : "",
      "udpkey"                : "",
      "otpkey"                : "",
      "target_server_ip"      : "",
      "target_server_port"    : ""
    }
  ]
}
```

Close and run again `capyknock_server.py`, it will now start on selected network interface. Server is ready.

```
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

[*] Importing modules...
[*] Loading conf file...
[*] Cleanup firewall...
[*] Loading firewall...
[*] Available interfaces...
      if0: Local Area Connection* 8
      if1: Local Area Connection* 7
      if2: Local Area Connection* 6
      if3: Bluetooth Network Connection 8
      if4: Local Area Connection* 10
      if5: Local Area Connection* 9
      if6: Ethernet 3
      if7: Wi-Fi
      if8: Loopback Adapter
      if9: VPN - VPN Client
      if10: VPN2 - VPN Client
      if11: Ethernet
[*] Sniffer started on interface : ['Wi-Fi', 'Loopback Adapter']
[*] Looking for UDP packets on port 45091
```

## Configure the Client

Open the `capyknock_client-conf.json` and copy details got from `capyknock_keygen.py`

```
{
      "username"              : "o73Z2SHNs029eUZxosVBFw51",
      "udpkey"                : "F9DprZJS0CJcmSRVHPFa_vc9nJzD3Rkc8USoNQO2J7o=",
      "otpkeydesc"            : "plinio@myserver",
      "knock_server_ip"       : "127.0.0.1",
      "knock_server_port"     : "45091",
      "target_server_ip"      : "127.0.0.1",
      "target_server_port"    : "22"
}
```

Run the client `capyknock_client.py`, you will be prompted to inser the OTP code that you see in the authenticator app (like Google Authenticator). The client will send the request to open port 22 and then try to open a TPC connection on the same, if it succeed, it will call [https://github.com/plinioseniore/capyknock/blob/main/capyknock_client.py#L51](nextauthentication).

```
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

[*] Loading conf file...
Enter the OTP code for plinio@myserver: 185478
Request to open port 22 on server 127.0.0.1 sent.....
Failed to open port 22 on target 127.0.0.1. Retry or contact a system administrator.
Enter the OTP code for plinio@myserver:
```

In this case the port 22 is not open and will prompt to retry.

On the server side you should get

```
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

[*] Importing modules...
[*] Loading conf file...
[*] Cleanup firewall...
[*] Loading firewall...
[*] Available interfaces...
      if0: Local Area Connection* 8
      if1: Local Area Connection* 7
      if2: Local Area Connection* 6
      if3: Bluetooth Network Connection 8
      if4: Local Area Connection* 10
      if5: Local Area Connection* 9
      if6: Ethernet 3
      if7: Wi-Fi
      if8: Loopback Adapter
      if9: VPN - VPN Client
      if10: VPN2 - VPN Client
      if11: Ethernet
[*] Sniffer started on interface : ['Wi-Fi', 'Loopback Adapter']
[*] Looking for UDP packets on port 45091
 > Received UDP message from username : o73Z2SHNs029eUZxosVBFw51 from IP 127.0.0.1
 > Received UDP message from username : o73Z2SHNs029eUZxosVBFw51 from IP 127.0.0.1
 > Received UDP message from username : o73Z2SHNs029eUZxosVBFw51 from IP 127.0.0.1
 >> Found user : o73Z2SHNs029eUZxosVBFw51 / plinio
 >>> Decrypted payload : {"otpcode": "185478", "trgsrvip": "127.0.0.1", "trgsrvport": "22", "myip": "", "hash": ""}
 >>>> Format of OTP code is valid
 >>>>> Authentication succesfull, OTP code is valid.
 >>>>>> The IP address is not banned
 >>>>>> Target server IP address match
 >>>>>> Target server IP port match
 >>>>>>> Open firewall rule for IP address in the IP packet
New-NetFirewallRule : Access is denied.
At line:1 char:1
+ New-NetFirewallRule -DisplayName '_capyknock_326' -Direction Inbound  ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (MSFT_NetFirewallRule:root/standardcimv2/MSFT_NetFirewallRule) [New-Ne
   tFirewallRule], CimException
    + FullyQualifiedErrorId : Windows System Error 5,New-NetFirewallRule

 >>>>>>> The IP address is already included in the allow list or has not been added in the firewall.
```

The server is not running as Administrator and failed to add the new firewall rule.

Re-run the server as Administrator and ensure something is listening on the `target_server_port` and you should get it working.
 
## Share the Secretes

As capyknock is based on symmetric encryption, you need to establish a secure communication path to share the secrets. On the client side you have to share the following:
- The `capyknock_client-conf.json` already configured or the configuration data to insert inside, the secrets is the `udpkey`
- The image of the QR Code or the `OTP key`

Keep those two secrets separated and ensure that the QR Code image or the `OTP key` are not saved on the client PC, in this way the information in the `capyknock_client-conf.json` are not enough to complete an authentication. Ensure that files shared to client are encrypted, as example with 7zip.

If you don't want to share the QR Code as image, because you don't trust that the file will be deleted, you can use `capyknock_qrcode.py` and pass the `OTP key` via another mean of communication.

## Restrict Internet Access

The server doesn't send any response, so you can set the firewall to block any outbound connection for the server process. Incoming UDP packets are sniffed directly via libcap/Scapy and so is not required a specific allow rule for the inbound UDP packets, at same time, restricting inbound internet access for the process may result in Scapy not being able to access libcap.
When creating those rules in the firewall, ensure that they don't match the [rule prefix](https://github.com/plinioseniore/capyknock/blob/main/capyknock_winfirewall.py#L184) otherwise you can get errors while the server try to manipulate the rules.
