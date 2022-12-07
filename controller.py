from scraper_model import scraper_model

#communicates between the model and view
class controller:
    #initialized with the model being used
    def __init__(self, mod):
        self.model = mod

    #calls the model to run the scrape team function
    def scrape_team(self,tn,ty):
        self.model.scrape_team(tn, ty)

    #returns the players list from the model
    def get_playersDf(self):
        return self.model.playersDf
    
    #returns the players dataframe from the model
    def get_players(self):
        return self.model.players
