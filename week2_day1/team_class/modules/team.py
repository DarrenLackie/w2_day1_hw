class Team:
    def __init__(self, input_team_name, input_list_of_players, input_coach):
        self.team_name = input_team_name
        self.players = input_list_of_players
        self.coach = input_coach
        self.points = 0

    def add_player(self, input_new_player):
        self.players.append(input_new_player)

    def has_player(self, input_player_in_question):
        return input_player_in_question in self.players
    
    #   for player in self.players:
    #       if input_player_in_question == player:
    #       return True
    #   return False

    def play_game(self, input_win_or_lose):
        if input_win_or_lose:
            self.points += 3
        
        # won_the_game = True
        # if input_win_or_lose == won_the_game:
        #     self.points += 3  

