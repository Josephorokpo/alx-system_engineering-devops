#0x13. Firewall

***ALX Software Engineering Project***


# The aim of this project is to install and configure a ufw firewall to block all incoming traffic except TCP prots 22, 80 and 443 on web-01, web-02 and lb-01 servers.

# Tasks

0. Block all incoming traffic but

Install the ufw firewall and setup a few rules on web-01.

Requirements:

The requirements below must be applied to web-01 (feel free to do it on lb-01 and web-02, but it won’t be checked)
Configure ufw so that it blocks all incoming traffic, except the following TCP ports:
22 (SSH)
443 (HTTPS SSL)
80 (HTTP)
Share the ufw commands that you used in your answer file

1. Port forwarding
 
Port forwarding

Requirements:

Configure web-01 so that its firewall redirects port 8080/TCP to port 80/TCP.
