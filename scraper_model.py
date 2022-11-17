import requests
import re
import constants

class scraper_model:
    def __new__(cls):
    #Singleton
        if not hasattr(cls, 'instance'):
            cls.instance = super(scraper_model, cls).__new__(cls)
        return cls.instance
    def __init__(self):
        self.playerIterator = None
        self.roster = None
        self.players = []
    def scrape_team(self, team_name, team_year):
        URL = "https://www.basketball-reference.com/teams/{}/{}.html".format(constants.TEAM_NAME_ACRONYM[team_name], team_year)
        r = requests.get(URL)