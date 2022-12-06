import streamlit as st
import pandas as pd
from constants import TEAM_NAME_ACRONYM
from strategy import NoScoreStrategy
from strategy import HighScoreStrategy
from strategy import LowScoreStrategy

class side_module:
    def __init__(self, con, score_strategy):
        self.controller = con
        self.scoreStrat = score_strategy

    def display_side_module(self): 
        with st.sidebar:
            self.scoreStrat.showScore()
            
            team_name = st.text_input("Team Name")
            yearString = st.text_input("Year")
            
            year = 0
            if yearString != '':
                year = int(yearString)
            
            st.write("Please use glossary to find team names, and enter in a year from 1979 to present. \n")
            
            if(team_name not in TEAM_NAME_ACRONYM or year > 2022 or year < 1979):
                if year != 0:
                    st.write("Invalid input")
            else:
                self.controller.scrape_team(team_name, year)
                
                