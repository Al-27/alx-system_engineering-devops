#!/usr/bin/python3
import requests
from sys import argv

def number_of_subscribers(subreddit):
    resp = requests.get(f"https://api.reddit.com/r/{subreddit}/about")
    try:
        subs = resp.json().get('data').get('subscribers')
        return subs if subs is not None else 0
    except Exception :
        return 0
    
if __name__ == "__main__":
    print(number_of_subscribers(argv[1]))