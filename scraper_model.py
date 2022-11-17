import requests

class scraper_model:
    def __init__(self):
        self.cur_data = {}
        self.playerIterator = None
        self.roster = None
    def scrape_team(self, team_name, team_year):
        URL = "https://www.basketball-reference.com/teams/{}/{}.html"
        r = requests.get(URL)
        print(r.content)