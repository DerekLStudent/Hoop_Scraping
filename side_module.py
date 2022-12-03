import streamlit as st
import pandas as pd
from constants import TEAM_NAME_ACRONYM

class side_module:
    def __init__(self, con):
        self.controller = con

    def display_side_module(self): 
        with st.sidebar:
            team_name = st.text_input("Team_name")
            year = int(st.text_input("year"))
            if(team_name not in TEAM_NAME_ACRONYM or year > 2022 or year < 1979):
                st.write("invalid input")
            else:
                self.controller.scrape_team(team_name, year)