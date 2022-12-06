#Code Taken from Bruce's L11 Slides on Strategy

import abc # Python's built-in abstract class library
import streamlit as st

class ScoreStrategyAbstract(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def showScore(self):
        """Required Method"""
    
class HighScoreStrategy(ScoreStrategyAbstract):
    def showScore(self):
        st.header("Your roster is good at scoring!")
        
class LowScoreStrategy(ScoreStrategyAbstract):
    def showScore(self):
        st.header("Your roster is not great at scoring...")
        
class NoScoreStrategy(ScoreStrategyAbstract):
    def showScore(self):
        st.header("Build a team that can score!")