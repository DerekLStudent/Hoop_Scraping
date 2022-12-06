from scraper_model import scraper_model

class controller:
    def __init__(self, mod):
        self.model = mod

    def scrape_team(self,tn,ty):
        self.model.scrape_team(tn, ty)

    def get_playersDf(self):
        return self.model.playersDf
    
    def get_players(self):
        return self.model.players
