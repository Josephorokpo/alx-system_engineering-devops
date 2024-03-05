#!/usr/bin/python3

"""
This module provides a recursive function to query the Reddit API and return a
list containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    Recursively query the Reddit API and return a list containing the
    titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): List to store the titles of hot articles.

    Returns:
        list: List containing the titles of all hot articles for the given
        subreddit, or None if no results are found.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    params = {'limit': 100}  # Request 100 posts per page

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if len(posts) == 0:
            return hot_list
        else:
            for post in posts:
                hot_list.append(post['data']['title'])
            # Get the name of the last post for pagination
            last_post_name = posts[-1]['data']['name']
            # Recursive call with the last post name as the after parameter for pagination
            return recurse(subreddit, hot_list, last_post_name)
    else:
        return None


if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    hot_articles = recurse(subreddit)
    if hot_articles is None:
        print("No results found for the given subreddit.")
    else:
        print("List of hot articles for", subreddit)
        for article in hot_articles:
            print(article)
