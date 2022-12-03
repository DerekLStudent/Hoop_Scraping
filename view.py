import streamlit as st
import pandas as pd
from side_module import side_module
class view:
    def __init__(self, con):
        self.controller = con
        self.side_module = side_module(con)
    def run_view(self):
        tab1, tab2 = st.tabs(["Team Builder", "Glossary"])
        with tab1:
            self.side_module.display_side_module()
            st.write(self.controller.get_playersDf())
        with tab2:
            st.write("glossary here!")