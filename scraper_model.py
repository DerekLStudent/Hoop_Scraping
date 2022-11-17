import requests
import re
import constants

class scraper_model:
    def __init__(self):
        self.cur_data = {}
        self.playerIterator = None
        self.roster = None
    def scrape_team(self, team_name, team_year):
        URL = "https://www.basketball-reference.com/teams/{}/{}.html".format(constants.TEAM_NAME_ACRONYM[team_name], team_year)
        r = requests.get(URL)
        print(re.search('Brad Stevens', r.text))