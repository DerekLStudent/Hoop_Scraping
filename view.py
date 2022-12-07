import streamlit as st
import pandas as pd

from side_module import side_module
from roster import roster
from constants import TEAM_NAME_ACRONYM
from strategy import NoScoreStrategy
from strategy import HighScoreStrategy
from strategy import LowScoreStrategy

#Controls how the data is being viewed using the streamlit library in Python
class view:
    #initializes the controller the view is connected to and a roster with a score strategy
    def __init__(self, con):
        self.controller = con
        
        #keeps the state of a roster even after streamlit reruns the code after an interaction
        if 'rosterState' not in st.session_state:
            st.session_state.rosterState = roster()
            
        #adds a text strategy object depending on the average score of the roster so far
        if len(st.session_state.rosterState.fullRoster) > 0:
            if st.session_state.rosterState.getAvgPoints() > 20:
                self.side_module = side_module(self.controller, HighScoreStrategy())
            else:
                self.side_module = side_module(self.controller, LowScoreStrategy())
        else:
            self.side_module = side_module(self.controller, NoScoreStrategy())
            
            
    #runs the main view seen in the local host
    def run_view(self):
        st.title("Hoop Scraping")
        self.side_module.display_side_module()  #side module displayed for searching team and year


        tab1, tab2, tab3 = st.tabs(["Team Builder", "Choose Players", "Roster"])
        
        #shows the player stats table of team scraped from basketball reference
        with tab1:
            if self.controller.get_playersDf() is not None:
                st.write(self.controller.get_playersDf())
            else:
                st.write("Enter a team name and year to find roster!")
            
        #shows checkbox list of player names to add to your roster
        with tab2:
            if self.controller.get_playersDf() is not None:
                for man in self.controller.get_players():
                    if st.checkbox(man.name + " " + str(man.year)):
                        st.session_state.rosterState.addToRoster(man)
            else:
                st.write("Search for a team to add players!")
            
        #shows the current roster
        with tab3:
            if len(st.session_state.rosterState.fullRoster) == 0:
                st.write("Roster is empty!")
            else:
                st.write(st.session_state.rosterState.rosterDF())
                
                #remove last player in roster button
                if st.button('Remove last player from roster'):
                    st.session_state.rosterState.clearLastPlayer()
                    st.write("New Roster Look")
                    st.write(st.session_state.rosterState.rosterDF())
                    
                #remove entire roster button
                if st.button('Clear entire roster'):
                    st.session_state.rosterState.clearRoster()
                    st.write("New Roster Look")
                    st.write(st.session_state.rosterState.rosterDF())
            
        