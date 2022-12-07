#SINGLETON DESIGN PATTERN USED

import requests
import re
import constants
from bs4 import BeautifulSoup
import pandas as pd

from player import player
from gamestats import gamestats

class scraper_model:
    #singleton instance function, only one instance of the scraper model needed
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(scraper_model, cls).__new__(cls)
        return cls.instance
    
    #initialize with a players list and players dataframe
    def __init__(self):
        self.players = []
        self.playersDf = None
        
    #using beautiful soup, scrape data of a given NBA team in a given year from www.basketball-reference.com
    def scrape_team(self, team_name, team_year):
        #ERROR NOTES: Teams before 3 point era have different tables
        
        #set player list and dataframe to empty
        self.players = []
        if self.playersDf != None:
            self.playersDf = self.playersDf.iloc[0:0]

        #set up scraper and retrieve data from team page
        URL = "https://www.basketball-reference.com/teams/{}/{}.html".format(constants.TEAM_NAME_ACRONYM[team_name], team_year)
        r = requests.get(URL).text
        soup = BeautifulSoup(r, 'html.parser')

        #build a dataframe with the main per game statistics we want to show for each player
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
        
        
        #build a dataframe with the main general facts we want to show for each player (year, position, height)
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
        
        #merger the two tables
        finalTable = rosterData.merge(statsData)
        
        #create player objects and fill them in the players list
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
            
        #set players dataframe
        self.playersDf = finalTable
        
        