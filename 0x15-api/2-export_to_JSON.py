#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to a JSON file."""
import requests
import sys
import json

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    tasks = [{"task": todo["title"], "completed": todo["completed"], "username": user["name"]} for todo in todos]

    json_data = {user_id: tasks}
    with open(f"{user_id}.json", "w") as json_file:
        json.dump(json_data, json_file)
