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

The single packet authorization (SPA) is an authentication approach that use a single encrypted packet to request access to a service behind a drop-any firewall filter. Implemented over a connectionless socket and without any reply, allow a stealth approach and can be used to shield frequently scanned TCP servers like SSH.
This approach reduce the opportunity to leverage 0-days or unpatched vulnerabilities as well as will help keeping logs clean.

## Implementation

The client communicate with the server sending a single UDP packet encrypted with a symmetric key and including in its payload an OTP value generated externally (like Microsoft Authenticator, Google Authenticator or any other time based OTP app). The server scans UDP message via [Scapy](https://github.com/secdev/scapy), without having an listening socket, try to decrypt the message and validate the TOTP code.

If successful, it will allow the client IP address in the firewall, so that as next step a TCP connection to the desired service can be started.

> WARNING!
> Do not use capyknock as the only authentication method, ensure that the service behind capyknock has its own authentication.

### Use Case

This approach is a good fit for servers with low number of users and generally speaking in cases in which you don't do often maintenance/upgrade of the server and so want to keep the server far from scans.

### Features

The following features are supported:
- Client to Server communication via single encrypted UDP packet
- Server sniff packets via Scapy / libcap
- Multiple users can be defined in the Server configuration file, each user with its own symmetric key
- Server side control of the allowed ports to open
- Keygen to ease the configuration
- Resistance to replay attack, reused TOTP are discarded

By design, capyknock is currently not resistant to MITM. To avoid dependency from external services, the client doesn't encode in the payload it IP address and the server trust the IP address in the IP header. So potentially, a MITM is possible changing the IP header.
This because is assumed that MITM is an edge case for a tool like capyknock where the main goal is to reduce the attack surface from external scanners.

Anyhow the JSON message sent from client to server has already a field to specify the IP address, the server already use that field if filled. So changing the client code to specify the IP address will make capyknock resistant to MITM.

## Dependencies and Run

Install the following to run capyknock:

```
pip install scapy
pip install cryptography
pip install pyotp
```

Ensure to have a libcap compatible software that is supported by [Scapy](https://github.com/secdev/scapy).

Then run the capyknock py script as needed.

## Why capyknock

There is no longer active developement of [fwknop](https://github.com/mrash/fwknop/), that is still based on iptables and have no Windows server implementation. Rather [pyknock](https://github.com/Snawoot/pyknock) has no server side control of the allowed users and ports to open.

Is it based on Python so that can be easily modified, as example to define the action after the SPA is successful.

## Supported Operative Systems

The code client and server itself can run wherever Python can run, but the current firewall manipulation is for Windows and based on PowerShell. To run on different OS than Windows is required to write dedicated firewall manipulation rules. 

## Build

To build an executable, use [pyinstaller](https://github.com/pyinstaller/pyinstaller) keeping in mind that it will build executables for the system on which in running. For Windows x64 are included the `.spec files` for server and client build.

If not done yet, install [pyinstaller](https://github.com/pyinstaller/pyinstaller)
```
pip install pyinstaller
```

On Windows 64 bits :
```
build_win_x64.bat
```

On any other platform supported by [pyinstaller](https://github.com/pyinstaller/pyinstaller) :
```
pyi-makespec capyknock_server.py
pyi-makespec capyknock_banip.py
pyi-makespec capyknock_keygen.py
pyi-makespec capyknock_client.py
```
Optionally the `.spec files` `capyknock_server.spec`, `capyknock_banip.spec` and `capyknock_keygen.spec` can be merged into a single `.spec file` as per instruction [here](https://github.com/orgs/pyinstaller/discussions/6634). This will create for each of those an executable file in the same distribution folder.

Assuming the merged file is called `capyknock_server.spec`, the running
```
pyinstaller capyknock_server.spec
pyinstaller capyknock_client.spec
```

## First Run

See this [FIRSTRUN.md](step by step guide)

## ASCII Art

From [Emoji Combos](https://emojicombos.com/capybara)
