import requests
import re
import constants
from bs4 import BeautifulSoup
import pandas as pd

from player import player
from gamestats import gamestats
from roster import roster

class scraper_model:
    def __new__(cls):
        #Singleton
        if not hasattr(cls, 'instance'):
            cls.instance = super(scraper_model, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        self.playerIterator = None
        self.players = []
        self.playersDf = None
        
    def displayRoster(self):
        self.roster.displayFullRoster()
        
    def displayPlayersSearched(self, team_name, team_year):
        print(team_year, team_name, "roster")
        
        for foundPlayer in self.players:
            foundPlayer.displayPlayer()
            print()
        
    def scrape_team(self, team_name, team_year):
        #ERROR NOTES: Teams before 3 point era have different tables
        
        self.players = []
        if self.playersDf != None:
            self.playersDf = self.playersDf.iloc[0:0]

        URL = "https://www.basketball-reference.com/teams/{}/{}.html".format(constants.TEAM_NAME_ACRONYM[team_name], team_year)
        r = requests.get(URL).text
        
        soup = BeautifulSoup(r, 'html.parser')


        perGameTable = soup.find('table', id='per_game')
        perGameHeaders = ['Name','PPG','RPG','APG','SPG','BPG','2P%','3P%','FT%','MPG']
        statsData = pd.DataFrame(columns = perGameHeaders)
        
        for row in perGameTable.tbody.find_all('tr'):
            columns = row.find_all('td')
            
            statsData = statsData.append({
                'Name': columns[0].text,
                'PPG': columns[26].text,
                'RPG': columns[20].text,
                'APG': columns[21].text,
                'SPG': columns[22].text,
                'BPG': columns[23].text,
                '2P%': columns[13].text,
                '3P%': columns[10].text,
                'FT%': columns[17].text,
                'MPG': columns[4].text,
            }, ignore_index=True)
        
        
        rosterTable = soup.find('table', id='roster')
        rosterHeaders = ['Name','Year','Pos','Ht']
        rosterData = pd.DataFrame(columns = rosterHeaders)
        
        for row in rosterTable.tbody.find_all('tr'):
            columns = row.find_all('td')
            
            rosterData = rosterData.append({
                'Name': columns[0].text,
                'Year': team_year,
                'Pos': columns[1].text,
                'Ht': columns[2].text
            }, ignore_index=True)
        
        finalTable = rosterData.merge(statsData)
        
        
        for i in finalTable.index:
            currStats = gamestats(finalTable['PPG'][i],
                                  finalTable['RPG'][i],
                                  finalTable['APG'][i],
                                  finalTable['SPG'][i],
                                  finalTable['BPG'][i],
                                  finalTable['FT%'][i],
                                  finalTable['2P%'][i],
                                  finalTable['3P%'][i],
                                  finalTable['MPG'][i],)
            
            self.players.append(player(finalTable['Name'][i], finalTable['Year'][i], finalTable['Pos'][i], finalTable['Ht'][i], currStats))
            
        self.playersDf = finalTable
        
        