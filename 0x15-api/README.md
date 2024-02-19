#0x15. API

***ALX Software Engineering Programme Project***

In this project, I learned about various concepts and practices related to scripting and programming. I gained insights into what Bash scripting should not be used for and delved into understanding the fundamentals of APIs, including the concepts of REST APIs and microservices. Additionally, I familiarized myself with the CSV and JSON formats, which are commonly used for data interchange. Moreover, I explored Pythonic naming conventions for packages, modules, classes, variables, functions, and constants, understanding the significance of using CapWords or CamelCase in Python for better code readability and consistency.

#Tasks

0. Gather data from an API

0-gather_data_from_an_API.py: Python script that returns information on the to-do list progress of a given employee ID.
Usage: python3 0-gather_data_from_an_API.py <employee ID>.
Output: Employee <employee name> is done with tasks(<# completed tasks>/<total # tasks>):

1. Export to CSV

1-export_to_CSV.py: Python script exports to-do list information of a given employee ID to CSV format.
Usage: python3 1-export_to_CSV.py <employee ID>
File name: <user id>.csv.
Format: "<user id>","<username>","<task completed status>","<task title>".

2. Export to JSON

2-export_to_JSON.py: Python script that exports to-do list information of a given employee ID to JSON format.
Usage: python3 2-export_to_JSON.py <employee ID>
File name: <user id>.json
Format: { "<user id>": [ {"task": "<task title>", "completed": <task completed status>, "username": "<username>"}}, ... ]}

3. Dictionary of list of dictionaries

3-dictionary_of_list_of_dictionaries.py: Python script that exports to-do list information for all employees to JSON format.
Usage: python3 3-dictionary_of_list_of_dictionaries.py
File name: todo_all_employees.json
Format: { "<user id>": [ {"username": "<username>", "task": "<task title>", "completed": <task completed status>}, {"username": "<username>", "task": "<task title>", "completed": <task completed status>}, ... ], "<user id>": [ {"username": "<username>", "task": "<task title>", "completed": <task completed status>}, {"username": "<username>", "task": "<task title>", "completed": <task completed status>}, ... ]}
