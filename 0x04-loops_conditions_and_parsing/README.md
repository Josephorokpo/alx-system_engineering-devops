#0x04. Loops, Conditions, and Parsing
***ALX Software Engineering Project***

#Learning Objectives
Upon completion of this project, I am expected to:

-Create SSH keys for secure server access.
-Understand the advantages of using #!/usr/bin/env bash over #!/bin/bash.
-Master the use of while, until, and for loops.
-Implement if, else, elif, and case condition statements.
-Utilize the cut command for text manipulation.
-Learn and apply file and other comparison operators.

#Requirements

-Allowed Editors: vi, vim, emacs
-Interpreter: Ubuntu 20.04 LTS
-File Ending: All files should end with a new line
-README.md: A mandatory file explaining the project.
-Script Executability: All Bash script files must be executable.
-Shellcheck: Ensure all Bash scripts pass Shellcheck (version 0.7.0) without errors.
-First Line: The first line of all Bash scripts should be exactly #!/usr/bin/env bash.
-Second Line: The second line of all Bash scripts should be a comment explaining the script's purpose.

#Tasks

0. Create a SSH RSA key pair
-Generate a RSA key pair.
-Share the public key in 0-RSA_public_key.pub.
-Fill the SSH public key field of your intranet profile.
-Keep the private key secure for future server access.

Repo:

GitHub: alx-system_engineering-devops
Directory: 0x04-loops_conditions_and_parsing
File: 0-RSA_public_key.pub

1. For Best School loop
-Use a for loop to display "Best School" 10 times.

Repo:

GitHub: alx-system_engineering-devops
Directory: 0x04-loops_conditions_and_parsing
File: 1-for_best_school

2. While Best School loop
-Display "Best School" 10 times using a while loop.

Repo:

GitHub: alx-system_engineering-devops
Directory: 0x04-loops_conditions_and_parsing
File: 2-while_best_school

3. Until Best School loop
-Use an until loop to display "Best School" 10 times.

Repo:

GitHub: alx-system_engineering-devops
Directory: 0x04-loops_conditions_and_parsing
File: 3-until_best_school

4. If 9, say Hi!
-Display "Best School" 10 times, but for the 9th iteration, display "Hi" on a new line.

Repo:

GitHub: alx-system_engineering-devops
Directory: 0x04-loops_conditions_and_parsing
File: 4-if_9_say_hi

5. 4 bad luck, 8 is your chance
-Loop from 1 to 10 and display:
 -"bad luck" for the 4th iteration
 -"good luck" for the 8th iteration
 -"Best School" for other iterations

Repo:

GitHub: alx-system_engineering-devops
Directory: 0x04-loops_conditions_and_parsing
File: 5-4_bad_luck_8_is_your_chance

6. Superstitious numbers
-Display numbers from 1 to 20 and:
 -"bad luck from China" for the 4th iteration
 -"bad luck from Japan" for the 9th iteration
 -"bad luck from Italy" for the 17th iteration

Repo:

GitHub: alx-system_engineering-devops
Directory: 0x04-loops_conditions_and_parsing
File: 6-superstitious_numbers

7. Clock
-Display the time for 12 hours and 59 minutes.

Repo:

GitHub: alx-system_engineering-devops
Directory: 0x04-loops_conditions_and_parsing
File: 7-clock

8. For ls
-Display the content of the current directory in a list format, showing hidden files.

Repo:

GitHub: alx-system_engineering-devops
Directory: 0x04-loops_conditions_and_parsing
File: 8-for_ls

9. To file, or not to file
-Display information about the file named iamfile.

Repo:

GitHub: alx-system_engineering-devops
Directory: 0x04-loops_conditions_and_parsing
File: 9-to_file_or_not_to_file

10. FizzBuzz
-Write a Bash script that displays numbers from 1 to 100

Repo:

GitHub repository: alx-system_engineering-devops
Directory: 0x04-loops_conditions_and_parsing
File: 10-fizzbuzz

11. Read and cut
Write a Bash script that displays the content of the file /etc/passwd.

Repo:

GitHub repository: alx-system_engineering-devops
Directory: 0x04-loops_conditions_and_parsing
File: 100-read_and_cut

12. Tell the story of passwd
Write a Bash script that displays the content of the file /etc/passwd, using the while loop + IFS.

Repo:

GitHub repository: alx-system_engineering-devops
Directory: 0x04-loops_conditions_and_parsing
File: 101-tell_the_story_of_passwd

13. Let's parse Apache logs
Write a Bash script that displays the visitor IP along with the HTTP status code from the Apache log file.

Repo:

GitHub repository: alx-system_engineering-devops
Directory: 0x04-loops_conditions_and_parsing
File: 102-lets_parse_apache_logs

14. Dig the data
Using what you did in the previous exercise, write a Bash script that groups visitors by IP and HTTP status code, and displays this data.

Repo:

GitHub repository: alx-system_engineering-devops
Directory: 0x04-loops_conditions_and_parsing
File: 103-dig_the-data
