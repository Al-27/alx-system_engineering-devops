#!/usr/bin/python3
"""
this is a doc
"""
import requests
from sys import argv

def number_of_subscribers(subreddit):
    resp = requests.get(f"https://api.reddit.com/r/{subreddit}/about",allow_redirects=False)
    try:
        subs = resp.json().get('data').get('subscribers')
        return subs if subs is not None else 0
    except Exception :
        return 0
