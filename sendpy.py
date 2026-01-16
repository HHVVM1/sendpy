import requests

def token(t="token: "):
    return input(t)

def id(i="id: "):
    return input(i)

def send(msg="", token="", id=""):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.post(url, json={'chat_id': id, 'text': msg})