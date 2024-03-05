#!/usr/bin/python3

"""
This module provides a recursive function to query the Reddit API, parse the
titles of all hot articles, and print a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, word_counts=None):
    """
    Recursively query the Reddit API, parse the titles of all hot articles, and
    print a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count.
        word_counts (dict): Dictionary to store the count of each keyword.

    Returns:
        None
    """
    if word_counts is None:
        word_counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    params = {'limit': 100}  # Request 100 posts per page

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if len(posts) == 0:
            # No more posts to fetch, print the sorted count of keywords
            sorted_word_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_word_counts:
                print(f"{word.lower()}: {count}")
            return
        else:
            for post in posts:
                title = post['data']['title'].lower()
                # Split the title into words and count occurrences of keyword
                for word in word_list:
                    if word.lower() in title.split():
                        word_counts[word.lower()] = word_counts.get(word.lower(), 0) + 1
            # Get the name of the last post for pagination
            last_post_name = posts[-1]['data']['name']
            # Recursive call with the last post name as the after pagination
            return count_words(subreddit, word_list, word_counts, last_post_name)
    else:
        return None


if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    word_list = input("Enter keywords separated by spaces: ").split()
    print("Keyword counts:")
    count_words(subreddit, word_list)
