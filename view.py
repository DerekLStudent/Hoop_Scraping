import streamlit as st
import pandas as pd
from side_module import side_module
from constants import TEAM_NAME_ACRONYM
class view:
    def __init__(self, con):
        self.controller = con
        self.side_module = side_module(con)
    def run_view(self):
        st.title("Hoop Scraping")

        tab1, tab2, tab3, tab4 = st.tabs(["Team Builder", "Choose Players", "Roster", "Glossary"])
        with tab1:
            self.side_module.display_side_module()
            st.write(self.controller.get_playersDf())
        with tab2:
            st.write("Player Buttons Here!")
        with tab3:
            st.write("Roster here!")
        with tab4:
            st.table(list(TEAM_NAME_ACRONYM))