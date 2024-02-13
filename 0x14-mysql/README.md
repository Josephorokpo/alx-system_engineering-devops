#0x14. MySQL

***ALX Software Engineering Programme Project***

In this project, I gained hands-on experience configuring database servers in a primary-replica architecture. Utilizing the two servers allocated by ALX, I set up a MySQL primary-replica configuration, establishing a connection between them and deploying a dummy database. Additionally, I developed a Bash script to streamline the process of generating database backups automatically.

#Tasks

4-mysql_configuration_primary: The MySQL my.conf configuration file used to set up my first server as a primary database server on the database tyrell_corp.

4-mysql_configuration_replica: The MySQL my.conf configuration file used to set up my second server as the replica database server on the database tyrell_corp.

5-mysql_backup: Bash script that generates a compressed tar.gz archive from a MySQL dump.

Usage: ./5-mysql_backup <MySQL root password>
Generates a dump containing all MySQL databases on the root server.
Names the resulting tar archive in the format day-month-year.tar.gz.
