from scraper_model import scraper_model
class controller:
    def __init__(self, mod):
        self.model = mod
    def model_set_PW(self, pw):
        self.model.password = pw
    def model_set_UN(self, un):
        self.model.username = un
    def scrape_courses(self, cname,clevel):
        self.model.scrape_courses(cname, clevel)
        #pass
    def scrape_profs(self, pname):
        pass