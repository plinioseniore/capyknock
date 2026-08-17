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

### Run the server
Install the following to run capyknock:

```
pip install scapy
pip install cryptography
pip install pyotp
```

Ensure to have a libcap compatible software that is supported by [Scapy](https://github.com/secdev/scapy).

Then run the capyknock_server py script as needed, read [FIRSTRUN.md](FIRSTRUN.md) for a step by step guide.

### Run the client
Install the following to run capyknock:

```
pip install cryptography
```

Then run the capyknock_client py script as needed, read [FIRSTRUN.md](FIRSTRUN.md) for a step by step guide.

## Why capyknock

There is no longer active development of [fwknop](https://github.com/mrash/fwknop/), that is still based on iptables and have no Windows server implementation. Rather [pyknock](https://github.com/Snawoot/pyknock) is designed for your own access and doesn't fit much a multi user scenario.

The use of Python ease the changes that can be required to fit your own needs. As example, modifying the action right after the authentication is successful.

## Supported Operative Systems

The code client and server itself can run wherever Python can run, but the current firewall manipulation (defined in `capyknock_winfirewall.py`) is for Windows and is based on PowerShell. To run the server on different OS than Windows is required to write dedicated firewall manipulation rules. 

Client runs either on Windows and Linux.

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

To protect more ports, runs multiple instances of capyknock, each instance will safeguard one port and should listed for SPA packets on a dedicated port. The current commit does no longer require to use a unique [rule prefix](https://github.com/plinioseniore/capyknock/blob/main/capyknock_winfirewall.py#L184) for each instance, because the port number is now added by default to the rule prefix.

## Workflow

Here the main steps of the workflow, for more details refer to the code of server and client itself:

The Client load the configuration file and check if the TCP port is already open, if so calls [nextauthentication(ip, port)](https://github.com/plinioseniore/capyknock/blob/main/capyknock_client.py#L144) and terminate itself :
- If the target TCP port is not open, Client ask the user to insert the OTP code and send the encrypted JSON. It wait for few seconds and then check again if the TCP port is open, it will loop asking a new OTP till the target TCP port is found open.
- Once the TCP port is found open, calls [nextauthentication(ip, port)](https://github.com/plinioseniore/capyknock/blob/main/capyknock_client.py#L144) and terminate itself. By default the [nextauthentication(ip, port)](https://github.com/plinioseniore/capyknock/blob/main/capyknock_nextaction.py) is empty, so you once the client close you can proceed connecting with the TCP service.

The server load the configuration and reads from libcap the UDP packets, if receive a JSON with the two expected fields it checks the following :
- It looks for a match of the username and if found, try to decrypt the payload with the associated symmetric key
- If decrypts succed, look for the OTP in the payload (that is a JSON itself)
- It calculate the current OTP with the associated key and compare with the OTP received from the client
- If above things are fine, create a allow entry in the firewall. This unless the IP is already within the allowed ones
- Every 12 hours goes for a firewall clean up, rules older than 2 days and with no active connection are deleted
- It listen for banrequest on localhost only, to be used by the inner authentication methond (like SSH fail2ban/IPBan) to request to ban an IP previously allowed by capyknock.

> WARNING! The username is in plaintext rather the payload is encrypted, so use a random username and not a real username in the server (like a Windows/SSH user). The configuration file generated with `capyknock_keygen.py` create a random username and then ask for a nickname. The nickname is not shared and is used in the configuration file as informative field, so that you can recall the user behind the random username.

The server keep a list of allowed IP address that is refreshed from the firewall at boot and every 12 hours, restarting the service does not affect IP already allowed and existing connections. Rather banned IPs are only in memory and can be reset with a reboot.

## Code Review

The code has been reviewed with free tier of Gemini, Copilot and Github Copilot. While Gemini and Copilot has given similar results, Github Copilot gave quite a different review, but none of those highlithed that the code is a single process running with administrative priviledges.

Running your own code review with those LLMs will likely gives similar results, here some notes that have not been considered and the reson behind:
 - Add a timestamp to the TOTP in the queue that prevents reusage. While adding a timestamp can reduce the validity window from 30s to a shorter one, this will not prevent an attacker to flood the server with valid request that can saturate the queue of used TOTP. To reach that point the attacker should have the keys and so is already able to craft a valid packet, it has no need to overfill the queue to reuse a TOTP sniffed from a previous packet. The TOTP is included in the encrypted payload, so pure sniffing is not applicable and reply the same packet within the validity windows will not overfill the queue.
 - Encrypt the username and verify the received packet against all the keys. The username is in clear and is suggested to be random (with a nickname that instead is private and will help to identify the user behind), this is seen as a Denial of Service vector. An attacker can use a sniffed username to have capyknock to evaluate the packet and burn CPU. Having the username encrypted is not really a fix, because it will require to verify a packet against all the keys, so that any packet will need to be evaluated, so DoS is still an option and is even amplified. The current implementation requries that the username is sniffed before be able to craft packet that will be processed and so attempt a DoS.
 - Add validation for external input in the functions even if the validation is done before passing the arguments. Generally speaking would be better to have redundancies in the validation than risk a missing validation, but in this specific case the function are used into a single path flow. There isn't a real risk that function get called by a branch path of the flow and miss a validation.
 
Something have instead been incldued, here some:
 - Use a Queue and not a Dequeue for the incoming packet, use a get() with timeout option instead of the sleep().
 - Use a single Queue that includes all the information to be processed and not two Dequeues that can loss synch.
 - Removing the shadowing of logging function.

## Secuirty Notice

To access the firewall and read from libcap, the code shall run with admin rights. In the current implementation, there is a single process that handle the messages sniffed via libcap, decrypt and then manipulate the firewall.
Running capyknock doesn't reveal to an external scan that the code is running, so is not possible for an external actor to identify the presence of this service and leverage any potential vulnerability. Anyhow the attack surface is the code itself and the the dependencies, that could be potentially exploited with a crafted message that address a specific vulnerability that could be there now or in the future.

The server doesn't send any response, so you can set the firewall to block any outbound connection for the server process. Incoming UDP packets are sniffed directly via libcap/Scapy and so is not required a specific allow rule for the inbound UDP packets, at same time, restricting inbound internet access for the process may result in Scapy not being able to access libcap.
When creating those rules in the firewall, ensure that they don't match the [rule prefix](https://github.com/plinioseniore/capyknock/blob/main/capyknock_winfirewall.py#L184) otherwise you can get errors while the server try to manipulate the rules.

## ASCII Art

From [Emoji Combos](https://emojicombos.com/capybara)
