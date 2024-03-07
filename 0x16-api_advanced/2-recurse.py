#!/usr/bin/python3
"""
this is a doc
"""
import requests


def recurse(subreddit):
    resp = requests.get(f"https://api.reddit.com/r/{subreddit}/hot?limit=100",
            headers={"HTTP_USER_AGENT": "checker:10.0.alx"}, allow_redirects=False)
    if resp.status_code != 200:
        return None
    try:
        posts = resp.json().get("data").get("children")
        list = [p.get('data').get('title') for p in posts]
        return list
    except Exception as e:
        return None
