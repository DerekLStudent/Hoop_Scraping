class roster:
    def __init__(self):
        self.fullRoster = []
        self.startingFive = []
        
    def addToRoster(self, player):
        if(len(self.fullRoster) < 15):
            self.fullRoster.append(player)
            print("Added", player.name, "to roster.")
        else:
            print("You can only have 15 players on a roster. Who do you want to remove?")
            self.displayFullRoster()
            
            
    def addToStartingFive(self, player):
        if(len(self.fullRoster) < 5):
            self.startingFive.append(player)
            print("Added", player.name, "to roster.")
        else:
            print("You can only have 5 players on your starting lineup. Who do you want to remove?")
            self.displayStartingFive()
            
    def displayFullRoster(self):
        for i in self.fullRoster:
            i.displayPlayer()
            
    def displayStartingFive(self):
        for i in self.startingFive:
            i.displayPlayer()
            