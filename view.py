import streamlit as st
import pandas as pd

from side_module import side_module
from roster import roster
from constants import TEAM_NAME_ACRONYM
from strategy import NoScoreStrategy
from strategy import HighScoreStrategy
from strategy import LowScoreStrategy

class view:
    def __init__(self, con):
        self.controller = con
        if 'rosterState' not in st.session_state:
            st.session_state.rosterState = roster()
            
        if len(st.session_state.rosterState.fullRoster) > 0:
            if st.session_state.rosterState.getAvgPoints() > 20:
                self.side_module = side_module(self.controller, HighScoreStrategy())
            else:
                self.side_module = side_module(self.controller, LowScoreStrategy())
        else:
            self.side_module = side_module(self.controller, NoScoreStrategy())
            
            
        
    def run_view(self):
        st.title("Hoop Scraping")
        self.side_module.display_side_module()

        tab1, tab2, tab3 = st.tabs(["Team Builder", "Choose Players", "Roster"])
        
        with tab1:
            if self.controller.get_playersDf() is not None:
                st.write(self.controller.get_playersDf())
            else:
                st.write("Enter a team name and year to find roster!")
            
        with tab2:
            if self.controller.get_playersDf() is not None:
                for man in self.controller.get_players():
                    if st.checkbox(man.name + " " + str(man.year)):
                        st.session_state.rosterState.addToRoster(man)
            else:
                st.write("Search for a team to add players!")
            
        with tab3:
            if len(st.session_state.rosterState.fullRoster) == 0:
                st.write("Roster is empty!")
            else:
                st.write(st.session_state.rosterState.rosterDF())
                
                if st.button('Remove last player from roster'):
                    st.session_state.rosterState.clearLastPlayer()
                    st.write("New Roster Look")
                    st.write(st.session_state.rosterState.rosterDF())
                    
                if st.button('Clear entire roster'):
                    st.session_state.rosterState.clearRoster()
                    st.write("New Roster Look")
                    st.write(st.session_state.rosterState.rosterDF())
            
        