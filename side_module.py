import streamlit as st
import pandas as pd

from constants import TEAM_NAME_ACRONYM
from strategy import NoScoreStrategy
from strategy import HighScoreStrategy
from strategy import LowScoreStrategy

#class for the side module seen in the view
class side_module:
    #initialized with the controller and score strategy to show
    def __init__(self, con, score_strategy):
        self.controller = con
        self.scoreStrat = score_strategy

    #display the side module
    def display_side_module(self): 
        team_names = [
            "Atlanta Hawks", "Boston Celtics", "Brooklyn Nets", "Charlotte Bobcats", "Chicago Bulls",
            "Cleveland Cavaliers", "Dallas Mavericks", "Denver Nuggets", "Detroit Pistons", "Golden State Warriors",
            "Houston Rockets", "Indiana Pacers", "Los Angeles Clippers", "Los Angeles Lakers", "Memphis Grizzlies",
            "Miami Heat", "Milwaukee Bucks", "Minnesota Timberwolves", "New Orleans Hornets", "New York Knicks",
            "Oklahoma City Thunder", "Orlando Magic", "Philadelphia 76ers", "Phoenix Suns", "Portland Trail Blazers",
            "Sacramento Kings", "San Antonio Spurs", "Toronto Raptors", "Utah Jazz", "Washington Wizards"
        ]
        
        with st.sidebar:
            self.scoreStrat.showScore() #Show score strategy text depending on roster ppg
            
            #Get nba team to scrape
            team_name = st.selectbox("Team Name", options=team_names)
            team_name = team_name.lower()
            
            #get year to scrape
            yearString = st.text_input("Year")
            year = 0
            if yearString != '':
                year = int(yearString)
            
            st.write("Please select a team and enter in a year from 1979 to present. \n")
            
            if(team_name not in TEAM_NAME_ACRONYM or year > 2022 or year < 1979):
                if year != 0:
                    st.write("Invalid input")
            else:
                self.controller.scrape_team(team_name, year) #scrape data for the nba team and year
                
                