import sys
import os
import json
import datetime
import requests
from bs4 import BeautifulSoup

url = input("Enter The URl Target: ")
urlRes = requests.get(url, timeout=1)

if urlRes.status_code == 200:
    print(f"The URL '{url}' has Res")
    soup = BeautifulSoup(urlRes.content, "html.parser")
    title = soup.find("title")
    body = soup.find("body")

    print(body.prettify())
