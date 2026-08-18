---
layout: default
---

## capyknock - Single Packet Authorization Port Knocking

### Hide your server from bot scans

I run a small server that jumps connection via SSH port forwarding to air-gapped machines. As anyone having an SSH service open to the world, the log files was full of russians and chineses people[^1] willing to became friends, not really something to be scared but annoing. In most of the cases there were some few tries per day with IPBan to take care, but there was a point in which I saw a pattern, multiple session at same time from the same IP tring to connect with different usernames, so that they could have tens of tries in a shot before IPBan kicked in. More, within a short time window, IP address from the same pool[^2] doing the same.

There was no reason my server could have been a target for someone, but I started looking for some port knocking, just to have some more peace of mind. I then came across [fwknop](https://github.com/mrash/fwknop) and liked a lot the idea to mix port knocking with encryption. With [fwknop](https://github.com/mrash/fwknop) your server services are hidden and only if you own the keys you can get the services accessible for your IP address.

The development of [fwknop](https://github.com/mrash/fwknop) stopped some years ago, is still based on iptables that are now deprecated, and the server cannot run on Windows[^3]. The rising of Wireguard [had influence on fwknop](https://github.com/mrash/fwknop/issues/344) because the main reason is getthing your services stealth and with Wireguard you can achieve the same result. Wireguard could answer my need partially, because I didn't want to deal with the installation of the VPN to my few users. The SSH client is portable and same should be for the this additional layer I was trying to add.

I the started looking for alternatives till decided to experiment with Python and code my own. I had two main needs that [fwknop](https://github.com/mrash/fwknop) didn't cover, Windows compatiblity and a less scary client. But the most important was something where I could put some capybara ASCII art.


### Coding capyknock

It didn't took much to code it, because most of the work is done by Python behind the scenes. The [capyknock](https://github.com/plinioseniore/capyknock) client ask for an OTP and then disappear, all the configuration is done in the file and it doesn't have a real UI. I can then setup a simple batch file that once the client close start the SSH connection. So even if you deal with two client the experience is almost seamless.

At the other end the [capyknock](https://github.com/plinioseniore/capyknock) server process the request and grant the access via the firewall, the communication is encrypted and only a client that owns the key can craft a packet that is accepted by the sever, that will otherwise discard it. The server cannot send a response, because it will break the single packet approach and stealthiness, so is the client that probe the TCP connection to understand if the request has been accepted.

Once coded the main question was if I was creating a bigger problem while trying to solve a problem that didn't exist. The single packet authorization is not an authentication method, so behind there is anyhow an authentication like the SSH one that is robust and field proven. So the question was, is my code reducing the attach surface or is creating a wider one?

The real answer is "who knows!?", but a reasonable answer is the surface is reduced and can be considered zero for an external bot. The server doesn't send replies and so can be restricted from internet access, it does execute powershell script but it does not use any parameter out of the IP address in those scripts. So is unlikely that can be abused to step in the server and is shielding well known services like SSH from scans and abuse via 0-days.

### Running capyknock

The instruction are included in the [Github readme](https://github.com/plinioseniore/capyknock/blob/main/README.md#dependencies-and-run) as well as [Windows-x64 binaries](https://github.com/plinioseniore/capyknock/releases) are available.


<hr>

[^1]: Yep, bots.
[^2]: At least likely from the same pool.
[^3]: Yep, I run a server on Windows, but trust me, is just laziness. I would have reinstalled the server on Linux.