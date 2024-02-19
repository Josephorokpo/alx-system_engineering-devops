#!/usr/bin/python3
"""Exports to-do list information for all employees to a JSON file."""
import requests
import sys
import json

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    
    # Dictionary to store tasks for all employees
    all_tasks = {}
    
    # Retrieve tasks for each employee
    for user_id in range(1, 11):  # Assuming there are 10 employees
        user = requests.get(url + "users/{}".format(user_id)).json()
        todos = requests.get(url + "todos", params={"userId": user_id}).json()
        
        # Extract tasks and format them
        tasks = [{"username": user["name"], "task": todo["title"], "completed": todo["completed"]} for todo in todos]
        
        # Store tasks for the current employee in the dictionary
        all_tasks[str(user_id)] = tasks
    
    # Write data to JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)
