#!/usr/bin/python3
"""Export TODO list information for a given employee ID to a CSV file."""
import csv
import sys
import requests

if __name__ == "__main__":
    # API endpoint URL
    url = "https://jsonplaceholder.typicode.com/"
    
    # Retrieve employee data
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    
    # Define CSV file name
    csv_file = "{}.csv".format(user_id)
    
    # Write data to CSV file
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos:
            writer.writerow([user["id"], user["username"], todo["completed"], todo["title"]])
