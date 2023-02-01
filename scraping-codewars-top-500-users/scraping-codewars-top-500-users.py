from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
import urllib.request
URL = "https://www.codewars.com/users/leaderboard"
from collections import UserList

def solution():
    with urllib.request.urlopen(URL) as f:
        class MyList(UserList):

            def __init__(self, data):
                super().__init__(data)

            def __getitem__(self, item):
                return self.data[item-1]
        
        class Leaderboard:
            def __init__(self):
                self.position = MyList([])
                
            def __getitem__(self, key):
                return self.position[key-1]
            
        class User:
            def __init__(self,rank , name ,honor,  clan="" ):
                self.rank = rank
                self.name = name
                self.clan = clan
                self.honor = honor

        
        soup = BeautifulSoup(f, 'html.parser')
        rank = soup.find_all("td", {"class": "rank is-small"})
        clan = soup.find_all("td", {"class": ""})
        honor = soup.find_all("td", {"class": "honor"})
        name = soup.find_all("td", {"class": "is-big"})

        leaderboard = Leaderboard()
        for i in range(500):
            user = User(int(rank[i].get_text().replace('#', '')), name[i].find("a").get_text(), int(honor[i].get_text().replace(',', '')), clan[i].get_text())
            leaderboard.position.append(user)
        
        return leaderboard