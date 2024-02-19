#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.
"""
import sys
import requests

if __name__ == "__main__":
    # API endpoint URL
    url = "https://jsonplaceholder.typicode.com/"
    
    # Retrieve employee data
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    
    # Count completed tasks
    completed_tasks = [todo["title"] for todo in todos if todo["completed"]]
    
    # Display employee's progress
    print("Employee {} is done with tasks({}/{}):".format(user["name"], len(completed_tasks), len(todos)))
    
    # Display titles of completed tasks
    for task in completed_tasks:
        print("\t{}".format(task))
