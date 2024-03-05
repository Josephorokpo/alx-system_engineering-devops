#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit_name):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit_name (str): The name of the subreddit.

    Returns:
        int: The number of subscribers if the subreddit is valid, otherwise 0.
    """

    if subreddit_name is None or type(subreddit_name) is not str:
        return 0

    response = requests.get(
        'http://www.reddit.com/r/{}/about.json'.format(subreddit_name),
        headers={
            'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)'
        }
    ).json()

    subscribers_count = response.get("data", {}).get("subscribers", 0)
    return subscribers_count
