# Web server

***ALX Software Engineering Programme Project***

During this project, I gained insights into the functioning of web servers and initiated the utilization of one. ALX provided a dedicated server for my use. I acquired the skills to employ scp and Fabric for file transfers to my server. Furthermore, I successfully performed a fundamental configuration of the server using Nginx.

The server is accessible at [bdbnb.site](http://bdbnb.site).

## Tasks:

* **0. Transfer a file to your server**
  * [0-transfer_file](./0-transfer_file): Bash script that transfers a file
  from Holberton's client to a server.
  * Accepts four arguments:
    * The path of the file to be transferred.
    * The IP of the server to transfer the file to.
    * The username that `scp` connects with.
    * The path of the SSH privtae key that `scp` uses.
  * `scp` transfers the file to the user home directory `~/`.

* **1. Install nginx web server**
  * [1-install_nginx_web_server](./1-install_nginx_web_server): Bash script
  that configures a new Ubuntu machine with Nginx.
  * Nginx listens on port 80.
  * When querying Nginx at its root `/` with a `curl` GET request,
  it returns a page containing the string `Hello World`.

* **2. Setup a domain name**
  * [2-setup_a_domain_name](./2-setup_a_domain_name): A text file containing
  the domain name set up for the server through Gandi.

* **3. Redirection**
  * [3-redirection](./3-redirection): Bash script that configures a new Ubuntu
  machine with Nginx.
  * Setup is identical to [1-install_nginx_web_server](./1-install_nginx_web_server)
  plus:
    * The location `/redirect_me` returns a `301 Moved Permanently` redirection
    to another page.

* **4. Not found page 404**
  * [4-not_found_page_404](./4-not_found_page_404): Bash script that configures
  a new Ubuntu machine with Nginx.
  * Setup is identical to [1-install_nginx_web_server](./1-install_nginx_web_server)
  plus:
    * Features a custom 404 page containing the string `Ceci n'est pas une page`.

* **5. Install Nginx web server (w/ Puppet)**
  * The manifest include resources to perform a 301 redirect when querying/redirect_me.
  * Nginx listens on port 80.
  * When querying Nginx at its root `/` with a `curl` GET request,
  it returns a page containing the string `Hello World`.
  * The redirection must be a “301 Moved Permanently”

 
