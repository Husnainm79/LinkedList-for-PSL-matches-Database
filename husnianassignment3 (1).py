class Player:
    def __init__(self, name):
        self.name = name
        self.next_player = None
        self.prev_player = None

class Match:
    def __init__(self, match_id, team1_name, team2_name, match_date, location):
        self.match_id = match_id
        self.team1_name = team1_name
        self.team2_name = team2_name
        self.match_date = match_date
        self.winner = None
        self.location = location
        self.team1_players = None  
        self.team2_players = None  
        self.next_match = None
        self.prev_match = None

class CricketMatchDatabase:
    def __init__(self):
        self.first_match = None  

    def add_match(self, match):
        new_match = match
        if not self.first_match:
            self.first_match = new_match
        else:
            current = self.first_match
            while current.next_match:
                current = current.next_match
            current.next_match = new_match
            new_match.prev_match = current

    def remove_match(self, match_id):
        current = self.first_match
        while current:
            if current.match_id == match_id:
                if current.prev_match:
                    current.prev_match.next_match = current.next_match
                if current.next_match:
                    current.next_match.prev_match = current.prev_match
                if current == self.first_match:
                    self.first_match = current.next_match
                del current
                print(f"Match {match_id} has been removed.")
                return
            current = current.next_match
        print(f"Match {match_id} not found.")

    def find_match(self, match_id):
        current = self.first_match
        while current:
            if current.match_id == match_id:
                return current
            current = current.next_match
        return None

    def print_matches_in_order(self):
        if not self.first_match:
            print("Cricket match database is empty.")
            return

        current = self.first_match
        while current:
            print(f"Match ID: {current.match_id}")
            print(f"Team 1: {current.team1_name}")
            if current.team1_players:
                print("Team 1 Players:")
                player = current.team1_players
                while player:
                    print(player.name)
                    player = player.next_player
            print(f"Team 2: {current.team2_name}")
            if current.team2_players:
                print("Team 2 Players:")
                player = current.team2_players
                while player:
                    print(player.name)
                    player = player.next_player
            print(f"Match Date: {current.match_date}")
            print(f"Winner: {current.winner}")
            print(f"Location: {current.location}")
            print()
            current = current.next_match

    def add_player_to_match(self, match_id, team, player_name):
        match = self.find_match(match_id)
        if match:
            new_player = Player(player_name)
            if team == 1:
                if not match.team1_players:
                    match.team1_players = new_player
                else:
                    player = match.team1_players
                    while player.next_player:
                        player = player.next_player
                    player.next_player = new_player
                    new_player.prev_player = player
            elif team == 2:
                if not match.team2_players:
                    match.team2_players = new_player
                else:
                    player = match.team2_players
                    while player.next_player:
                        player = player.next_player
                    player.next_player = new_player
                    new_player.prev_player = player
            print(f"Player {player_name} added to Match {match_id}")
        else:
            print(f"Match {match_id} not found.")

    def remove_player_from_match(self, match_id, team, player_name):
        match = self.find_match(match_id)
        if match:
            if team == 1:
                current = match.team1_players
            elif team == 2:
                current = match.team2_players

            while current:
                if current.name == player_name:
                    if current.prev_player:
                        current.prev_player.next_player = current.next_player
                    if current.next_player:
                        current.next_player.prev_player = current.prev_player
                    if team == 1:
                        match.team1_players = current.next_player
                    elif team == 2:
                        match.team2_players = current.next_player
                    del current
                    print(f"Player {player_name} removed from Match {match_id}")
                    return
                current = current.next_player
            print(f"Player {player_name} not found in Team {team} of Match {match_id}")
        else:
            print(f"Match {match_id} not found.")

def main():
    db = CricketMatchDatabase()

    match1 = Match("PSL1-1", "TeamA", "TeamB", "2023-01-01", "StadiumA")
    match2 = Match("PSL1-4", "TeamC", "TeamD", "2023-01-15", "StadiumB")
    match3 = Match("PSL2-1", "TeamX", "TeamY", "2023-02-05", "StadiumC")

    db.add_match(match1)
    db.add_match(match2)
    db.add_match(match3)

    db.add_player_to_match("PSL1-1", 1, "Player1")
    db.add_player_to_match("PSL1-1", 1, "Player2")
    db.add_player_to_match("PSL1-1", 2, "Player3")

    db.add_player_to_match("PSL1-4", 1, "Player4")

    print("Matches in the database:")
    db.print_matches_in_order()

    print("\nRemoving Player2 from PSL1-1:")
    db.remove_player_from_match("PSL1-1", 1, "Player2")
    db.print_matches_in_order()

if __name__ == "__main__":
    main()

