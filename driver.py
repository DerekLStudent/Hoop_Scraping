from scraper_model import scraper_model
from view import view
from controller import controller
import constants
class driver:
    def __init__(self):
        scrape_model = scraper_model()
        self.controller = controller(scrape_model)
        self.view = view(scrape_model, self.controller)
    
    def setup_model(self):
        #Initial setup for model.
        print("Please enter in an initial query to get started:")
        t_name = input("Please give a team name:").lower()
        t_year = int(input("Please give a year:"))
        if(t_name not in constants.TEAM_NAME_ACRONYM or t_year > 2022):
            print("invalid inputs, closing program.")
        self.controller.scrape_team(t_name, t_year)
    
    def run_scraping_instance(self):
        instance_done = False
        self.setup_model()
        while not instance_done:
            break
        print("Closing scraping instance!")