import re
from bs4 import BeautifulSoup
import urllib.request
def get_member_since(username):
    with urllib.request.urlopen("https://www.codewars.com/users/"+username) as f:
        soup = BeautifulSoup(f, 'html.parser')
        
        for i in soup.find_all("div", {"class": "stat"}):
            text = i.get_text()
            if text.startswith('Member Since:'):
                return text.replace('Member Since:', '')