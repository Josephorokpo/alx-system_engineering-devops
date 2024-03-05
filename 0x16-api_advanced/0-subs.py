#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0

    response = requests.get(
        'http://www.reddit.com/r/{}/about.json'.format(subreddit),
        headers={
            'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)'
        }
    ).json()

    subscribers = response.get("data", {}).get("subscribers", 0)
    return subscribers
