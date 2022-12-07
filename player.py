from gamestats import gamestats

#object that stores a players info and stats
class player:
    def __init__(self, name, year, position, height, stats):
        self.name = name
        self.year = year
        self.position = position
        self.height = height
        self.stats = stats  #gamestats object that has all the per game stats
        
    #print to console test function
    def displayPlayer(self):
        print("Name:", self.name)
        print("Year:", self.year)
        print("Pos:", self.position)
        print("Ht:", self.height)
        self.stats.displayStats()
    
        
        