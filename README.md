# capyknock - Single Packet Authorization Port Knocking
```
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣞⣆⢀⣠⢶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣀⡤⠤⠖⠒⠋⠉⣉⠉⠹⢫⠾⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⡏⢰⡴⠀⠀⠀⠉⠙⠟⠃⠀⠀⠀⠈⠙⠦⣄⡀⢀⣀⣠⡤⠤⠶⠒⠒⢿⠋⠈⠀⣒⡒⠲⠤⣄⡀⠀⠀⠀⠀⠀⠀
⢸⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠴⠂⣀⠀⠀   ⣴⡄⠉⢷⡄⠚⠀⢤⣒⠦⠉⠳⣄⡀⠀⠀⠀
⠸⡄⠼⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⣄⡂⠠⣀⠐⠍⠂⠙⣆⠀⠀
⠀⠙⠦⢄⣀⣀⣀⣀⡀⠀⢷⠀⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠰⡇⠠⣀⠱⠘⣧⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠉⢷⣧⡄⢼⠀⢀⠀⠀⠀⠀⠀capyknock     ⠀       ⠈  ⠀⡈⠀⢄⢸⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⡀⠃⠘⠂⠲⡀⠀⠀⠀         ⠀⠀    ⠀         ⠙⠀⡈⢘⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢫⡑⠣⠰⠀⢁⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀     ⠀⠁⣸⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣯⠂⡀⢨⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡆⣾⡄⠀⠀⠀⠀    ⣀⠐⠁⡴⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⡈⡀⢠⣧⣤⣀⣀⡀⢀⡀⠀⠀⢀⣼⣀⠉⡟⠀⢀⡀⠘⢓⣤⡞⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⡁⢁⣸⡏⠀⠀⠀⠀⠁⠀⠉⠉⠁⠹⡟⢢⢱⠀⢸⣷⠶⠻⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡏⠈⡟⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠁⠀⠻⣧⠀⠀⣹⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡤⠚⠃⣰⣥⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠼⢙⡷⡻⠀⡼⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠟⠿⡿⠕⠊⠉⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣾⠉⣹⣷⣟⣚⣁⡼⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
```

This set of script has been inspired by [fwknop](https://github.com/mrash/fwknop/) and [pyknock](https://github.com/Snawoot/pyknock) that are port knocking solutions based around the single packet authorization approach.

## Single Packet Authorization

The single packet authorization (SPA) is an authentication approach that use a single encrypted packet to request access to a service behind a drop-any firewall filter. Implemented over a connectionless socket and without any reply, allow a stealth approach and can be used to shield frequently scanned TCP servers, like SSH.
This approach reduce the opportunity to leverage 0-days or unpatched vulnerabilities as well as will keep logs cleaner.

## Implementation

The client communicate with the server sending a single UDP packet encrypted with a symmetric key and including in its payload an OTP value generated externally (like Microsoft Authenticator, Google Authenticator or any other time based OTP app). The server scans UDP message via [Scapy](https://github.com/secdev/scapy), without having an listening socket, try to decrypt the message and validate the OTP code.

If successful, it will allow the client IP address in the firewall, so that as next step a TCP connection to the desired service can be started.

> WARNING!
> Do not use capyknock as the only authentication method, ensure that the service behind capyknock has its own authentication.

### Use Case

This approach is a good fit for servers with low number of users and generally speaking in cases in which you don't do often maintenance/upgrade of the server and so want to keep the server far from scans.

### Features

The following features are supported:
- Client to Server communication via single encrypted UDP packet
- Server sniff packets via Scapy / libcap, so you can restrict internet access to the server via firewall
- Multiple users can be defined in the Server configuration file, each user with its own symmetric key
- Server side control of the allowed ports to open
- Keygen to ease the configuration
- Resistance to replay attack, reused TOTP are discarded

By design, capyknock is currently not resistant to MITM. To avoid dependency from external services, the client doesn't encode in the payload its IP address and the server trust the one included in the IP header. So potentially, a MITM is possible changing the IP header. Is it assumed that MITM is an edge case for a tool like capyknock where the main goal is to reduce the attack surface from external scanners.

Anyhow the encrypted JSON message sent from client to the server has already a field to specify the IP address, the server already use that field if filled. So changing the client code to specify the IP address will make capyknock resistant to MITM.

## Dependencies and Run

Install the following to run capyknock:

```
pip install scapy
pip install cryptography
pip install pyotp
```

Ensure to have a libcap compatible software that is supported by [Scapy](https://github.com/secdev/scapy).

Then run the capyknock py script as needed, read [FIRSTRUN.md](FIRSTRUN.md) for a step by step guide.

## Why capyknock

There is no longer active development of [fwknop](https://github.com/mrash/fwknop/), that is still based on iptables and have no Windows server implementation. Rather [pyknock](https://github.com/Snawoot/pyknock) is designed for your own access and doesn't fit much a multi user scenario.

The use of Python ease the changes that can be required to fit your own needs. As example, modifying the action right after the authentication is successful.

## Supported Operative Systems

The code client and server itself can run wherever Python can run, but the current firewall manipulation (defined in `capyknock_winfirewall.py`) is for Windows and is based on PowerShell. To run on different OS than Windows is required to write dedicated firewall manipulation rules. 

## Build

To build an executable, use [pyinstaller](https://github.com/pyinstaller/pyinstaller) keeping in mind that it will build executables for the operative system on which you run it. For Windows x64 are included the `.spec files` for server and client build.

### Windowx x64

If not done yet, install [pyinstaller](https://github.com/pyinstaller/pyinstaller)

```
pip install pyinstaller
```

On Windows 64 bits :
```
build_win_x64.bat
```

### Other Operative Systems

On any other platform supported by [pyinstaller](https://github.com/pyinstaller/pyinstaller) :
```
pyi-makespec capyknock_server.py
pyi-makespec capyknock_banip.py
pyi-makespec capyknock_keygen.py
pyi-makespec capyknock_client.py
pyi-makespec capyknock_qrcode.py
```

For server side build, optionally the `.spec files` `capyknock_server.spec`, `capyknock_banip.spec` and `capyknock_keygen.spec` can be merged into a single `.spec file` as per instruction [here](https://github.com/orgs/pyinstaller/discussions/6634). This will create for each of those an executable file in the same distribution folder.

For client side build, optionally the `.spec files` `capyknock_client.spec` and `capyknock_qrcode.spec` can be merged into a single `.spec file` as per instruction [here](https://github.com/orgs/pyinstaller/discussions/6634). This will create for each of those an executable file in the same distribution folder.

Assuming the merged file are called `capyknock_server.spec` and `capyknock_client.spec`, then run:
```
pyinstaller capyknock_server.spec
pyinstaller capyknock_client.spec
```

## First Run

See this [step by step guide](FIRSTRUN.md)

## Workflow

Here the main steps of the workflow, for more details refer to the code of server and client itself:

The Client load the configuration file and check if the TCP port is already open, if so calls [nextauthentication(ip, port)](https://github.com/plinioseniore/capyknock/blob/main/capyknock_client.py#L51) and terminate itself :
- If the target TCP port is not open, Client ask the user to insert the OTP code and send the encrypted JSON. It wait for few seconds and then check again if the TCP port is open, it will loop asking a new OTP till the target TCP port is found open.


The server load the configuration and reads from libcap the UDP packets, if receive a JSON with the two expected fields it checks the following :
- It looks for a match of the username and if found, try to decrypt the payload with the associated symmetric key
- If decrypts succed, look for the OTP in the payload (that is a JSON itself)
- It calculate the current OTP with the associated key and compare with the OTP received from the client
- If above things are fine, create a allow entry in the firewall. This unless the IP is already within the allowed ones
- Every 12 hours goes for a firewall clean up, rules older than 2 days and with no active connection are deleted
- It listed for banrequest on localhost only, to be used by the inner authentication methond (like SSH fail2ban/IPBan) to request to ban an IP previously allowed by capyknock.

> WARNING! The username is in plaintext rather the payload is encrypted, so use a random username and not a real username in the server (like a Windows/SSH user). The configuration file generated with `capyknock_keygen.py` create a random username and then ask for a nickname. The nickname is not shared and is used in the configuration file as informative field, so that you can recall the user behind the random username.

## Secuirty Notice

To access the firewall and read from libcap, the code shall run with admin rights. In the current implementation, there is a single process that handle the messages sniffed via libcap, decrypt and then manipulate the firewall.
Running capyknock doesn't revealt to an external scan that the code is running, so is not possible for an external actor to identify the presence of this service and leverage any potential vulnerability. Anyhow the attack surface is the code itself and the the dependencies, that could be potentially exploited with a crafted message that address a specific vulnerability that could be there now or in the future.

## ASCII Art

From [Emoji Combos](https://emojicombos.com/capybara)
