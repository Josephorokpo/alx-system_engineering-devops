0x0F. Load balancer

***ALX Software Engineering Programme Project***


In this project, I further developed the configuration of the web server initiated in project 0x0B. I received two additional servers: one to mirror the Nginx setup of the original server, and another to deploy an HAproxy load balancer to oversee both web servers.

#Tasks

0. Double the number of webservers

0-custom_http_response_header: Bash script that installs and configures Nginx on a server with a custom HTTP response header.
The name of the HTTP header is X-Served-By.
The value of the HTTP header is the hostname of the server.

1. Install your load balancer

1-install_load_balancer: Bash script that installs and configures HAproxy version 1.5 on a server.
Enables management via the init script.
Requests are distributed using a round-robin algorithm.
