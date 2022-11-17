class player:
    def __init__(self, name, year, position, height, stats):
        self.name = name
        self.year = year
        self.position = position
        self.height = height
        self.stats = stats
        self.inRoster = False
        
    def addToRoster(self):
        self.inRoster = True
        
    def removeFromRoster(self):
        self.inRoster = False
        
    def displayPlayer(self):
        print()
    
        
        