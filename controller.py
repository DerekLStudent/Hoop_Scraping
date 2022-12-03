from scraper_model import scraper_model
class controller:
    def __init__(self, mod):
        self.model = mod

    def scrape_team(self, tn,ty):
        self.model.scrape_team(tn, ty)
        #pass

    def get_playersDf(self):
        return self.model.playersDf

    # def add_player(self):
    #     if
    # def remove_player(self):
    # def get_roster(self):
    #     return self.model.roster