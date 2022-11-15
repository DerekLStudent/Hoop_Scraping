from scraper_model import scraper_model
from view import view
from controller import controller
class driver:
    def __init__(self):
        scrape_model = scraper_model()
        self.controller = controller(scrape_model)
        self.view = view(scrape_model, self.controller)
    def setup_model(self):
        print("To setup your scraping session, please enter in you username and password at the prompts")
        #TODO user input, then send it to controller to parameterize the model
        print("Please enter in an initial query to get started:")
        #TODO user input, then send it to to controller to start initial query in the model
    def run_scraping_instance(self):
        instance_done = False
        self.setup_model()
        while not instance_done:
            break
        print("Closing scraping instance!")