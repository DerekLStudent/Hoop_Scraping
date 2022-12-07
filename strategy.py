#STRATEGY DESIGN PATTERN USED

#Code Taken from Bruce's L11 Slides on Strategy

import abc # Python's built-in abstract class library
import streamlit as st

#abstract strategy object that displays a specific text based on a roster's average ppg
class ScoreStrategyAbstract(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def showScore(self):
        """Required Method"""
    
#displays text for a roster with a high scoring average
class HighScoreStrategy(ScoreStrategyAbstract):
    def showScore(self):
        st.header("Your roster is good at scoring!")
        
#displays text for a roster with a low scoring average
class LowScoreStrategy(ScoreStrategyAbstract):
    def showScore(self):
        st.header("Your roster is not great at scoring...")
        
#displays text for when a roster isn't built yet
class NoScoreStrategy(ScoreStrategyAbstract):
    def showScore(self):
        st.header("Build a team that can score!")