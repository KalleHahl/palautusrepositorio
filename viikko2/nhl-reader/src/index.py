import requests
from player import Player
import queue as Q

class PlayerReader():
    def __init__(self, url):
        self.url = url
    def fetch(self):
        return requests.get(self.url).json()
    
    def get_players(self):
        players = self.fetch()
        player_objects = []
        for player in players:
            player_obj = Player(player)
            player_objects.append(player_obj)
        return player_objects

class PlayerStats():
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):

        by_nationality_players = Q.PriorityQueue()
        players = self.reader.get_players()

        for player in players:
            if player.nationality == nationality:
                by_nationality_players.put((player))
      
        return by_nationality_players
    
        

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    print('Players from FIN\n')

    while not players.empty():
        print(players.get())
        

if __name__ == "__main__":
    main()
