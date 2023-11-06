class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.nationality = dict['nationality']

    def __str__(self):
        return f"{self.name:25}{self.team} {self.goals:2} + {self.assists:2} = {self.goals + self.assists}"
    
    def __lt__(self, other):
        return other.goals + other.assists < self.goals + self.assists

