#0x08. Networking basics #1
***ALX Software Engineering Project***

#Learning Objectives
At the end of this project, students are expected to be able to explain the following concepts:

>What is localhost/127.0.0.1
>What is 0.0.0.0
>What is /etc/hosts
>How to display your machine’s active network interfaces

#Requirements

>Allowed editors: vi, vim, emacs
>Interpreter: All your files will be interpreted on Ubuntu 20.04 LTS
>Line Endings: All your files should end with a new line
>README.md: A README.md file, at the root of the folder of the project, is mandatory
>Executable Bash Scripts: All your Bash script files must be executable
>Shellcheck: Your Bash script must pass Shellcheck (version 0.7.0 via apt-get) without any errors
>Shebang: The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
>Script Comment: The second line of all your Bash scripts should be a comment explaining what is the script doing

#Tasks

0. Change your home IP

Write a Bash script that configures an Ubuntu server with the below requirements.

Requirements:

>localhost resolves to 127.0.0.2
>facebook.com resolves to 8.8.8.8.

Repo:

GitHub repository: alx-system_engineering-devops
Directory: 0x08-networking_basics_2
File: 0-change_your_home_IP

1. Show attached IPs

Write a Bash script that displays all active IPv4 IPs on the machine it’s executed on.

Repo:

GitHub repository: alx-system_engineering-devops
Directory: 0x08-networking_basics_2
File: 1-show_attached_IPs


2. Port listening on localhost

Write a Bash script that listens on port 98 on localhost.

Terminal 0

Starting my script.

	sylvain@ubuntu$ sudo ./100-port_listening_on_localhost

Terminal 1

Connecting to localhost on port 98 using telnet and typing some text.

	sylvain@ubuntu$ telnet localhost 98
	Trying 127.0.0.2...
	Connected to localhost.
	Escape character is '^]'.
	Hello world
	test

	Terminal 0

Receiving the text on the other side.

	sylvain@ubuntu$ sudo ./100-port_listening_on_localhost
	Hello world
	test

Repo:

GitHub repository: alx-system_engineering-devops
Directory: 0x08-networking_basics_2
File: 100-port_listening_on_localhost

