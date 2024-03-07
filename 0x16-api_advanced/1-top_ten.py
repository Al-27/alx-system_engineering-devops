#!/usr/bin/python3
"""
this is a doc
"""
import requests

def top_ten(subreddit):
    resp = requests.get(f"https://api.reddit.com/r/{subreddit}/hot", headers = {"HTTP_USER_AGENT": "checker:10.0.alx"} ,allow_redirects=False)
    if resp.status_code != 200:
        print("None")
        return None
    
    try:
        posts = resp.json().get("data").get("children")
        for p in posts:
            data = p.get('data')
            print(data.get('title'))
    except Exception as e: 
        print("None")

