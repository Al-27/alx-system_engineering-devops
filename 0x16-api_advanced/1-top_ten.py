#!/usr/bin/python3
"""
this is a doc
"""
import requests
from sys import argv

def top_ten(subreddit):
    resp = requests.get(f"https://api.reddit.com/r/{subreddit}/hot", headers = {"HTTP_USER_AGENT": "chrome/10.0.0.1"} ,allow_redirects=False)
    if resp.status_code != 200:
        print("None")
        return
    
    try:
        posts = resp.json().get("data").get("children")
        for p in posts:
            data = p.get('data')
            print(data.get('title'))
    except Exception as e: 
        print(e)
