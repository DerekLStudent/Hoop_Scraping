import requests

class scraper_model:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.cur_data = {}
        self.course = None
        self.professor = None
        self.courseIterator = None
        self.cart = None
    def scrape_courses(self, class_name, class_level):
        URL = "https://classes.colorado.edu/"
        r = requests.get(URL)
        print(r.content)