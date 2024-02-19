#!/usr/bin/python3
"""
Exports TODO list information for a given employee ID to a JSON file.
"""
import json
import sys
import requests

if __name__ == "__main__":
    # API endpoint URL
    url = "https://jsonplaceholder.typicode.com/"
    
    # Retrieve employee data
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    
    # Define JSON file name
    json_file = "{}.json".format(user_id)
    
    # Prepare data for JSON export
    data = {"USER_ID": []}
    for todo in todos:
        data["USER_ID"].append({"task": todo["title"], "completed": todo["completed"], "username": user["username"]})
    
    # Write data to JSON file
    with open(json_file, mode='w') as file:
        json.dump(data, file)
