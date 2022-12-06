from scraper_model import scraper_model
from view import view
from controller import controller
import constants

class driver:
    def __init__(self):
        self.scrape_model = scraper_model()
        self.controller = controller(self.scrape_model)
        self.view = view(self.controller)
    
    def setup_model(self):
        #Initial setup for model.
        print("Please enter in an initial query to get started:")
        t_name = input("Please give a team name:").lower()
        t_year = int(input("Please give a year:"))
        if(t_name not in constants.TEAM_NAME_ACRONYM or t_year > 2022):
            print("invalid inputs, closing program.")
        self.controller.scrape_team(t_name, t_year)
    
    def run_scraping_instance(self):
        #self.setup_model()
        self.view.run_view()
        print("Ran Scraping Instance...")
        