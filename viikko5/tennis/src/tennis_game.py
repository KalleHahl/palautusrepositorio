from collections import defaultdict

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_point(self):
        self.score += 1

    def get_name(self):
        return self.name
    
    def get_score(self):
        return self.score

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.tie_scores = defaultdict(lambda: "Deuce")
        self.tie_scores.update({
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",

        })


    def won_point(self, player_name):
        if player_name == self.player1.get_name():
            self.player1.add_point()
        else:
            self.player2.add_point()
    
    def four_or_over(self, minus_result):
        if minus_result == 1:
            return "Advantage player1"
        elif minus_result == -1:
            return "Advantage player2"
        elif minus_result >= 2:
            return "Win for player1"
        else:
            return "Win for player2"
    
    def uneven_score(self,score, player1_score, player2_score):
        temp_score = 0
        for i in range(1, 3):
            if i == 1:
                temp_score = player1_score
            else:
                score = score + "-"
                temp_score = player2_score

            if temp_score == 0:
                score = score + "Love"
            elif temp_score == 1:
                score = score + "Fifteen"
            elif temp_score == 2:
                score = score + "Thirty"
            elif temp_score == 3:
                score = score + "Forty"
        return score




    def get_score(self):
        score = ""
        player1_score = self.player1.get_score()
        player2_score = self.player2.get_score()

        if player1_score == player2_score:
            score = self.tie_scores[player1_score]

        elif player1_score >= 4 or player2_score >= 4:
            minus_result = player1_score - player2_score
            score = self.four_or_over(minus_result)
        else:
            score = self.uneven_score(score, player1_score, player2_score)
            
        return score
