from basket_ball import *

def num_points_per_game(player_name):
    game_data = game_dict()  
    
    for team in ['home', 'away']:
        for player in game_data[team]['players']:
            if player['name'] == player_name:
                return player['points_per_game']
    
    return None

# player_name = "Rui Hachimura"
# points_per_game = num_points_per_game(player_name)
# if points_per_game is not None:
#     print(f"{player_name} scores {points_per_game} points per game.")
# else:
#     print(f"{player_name} was not found in the game data.")


def player_age(player_name):
    game_data = game_dict()

    for team in ['home', 'away']:
        for player in game_data[team]['players']:
            if player['name'] == player_name:
                return player['age']
            
    return None

# player_name = "Rui Hachimura"
# player_age = player_age(player_name)
# print(player_age)


def team_colors(team_name):
    game_data = game_dict()

    for team in ['home', 'away']:
        if game_data[team]['team_name'] == team_name:
            return game_data[team]['colors']
        
    return None

# team_name = 'Washington Wizards'
# print(team_colors(team_name))

def team_names():
    game_data = game_dict()

    return [game_data['home']['team_name'], game_data['away']['team_name']]

# names = team_names()
# print("Team names:", ", ".join(names))

def player_numbers(team_name):
    game_data = game_dict()

    for team in ['home', 'away']:
        if game_data[team]['team_name'] == team_name:
            return [player['number'] for player in game_data[team]['players']]
    
    return None

# team_name = "Cleveland Cavaliers"  
# jersey_numbers = player_numbers(team_name)
# if jersey_numbers is not None:
#     print(f"The jersey numbers of players in {team_name} are: {', '.join(map(str, jersey_numbers))}")
# else:
#     print(f"Team '{team_name}' was not found in the game data.")


def player_stats(player_name):
    game_data = game_dict()  

    for team in ['home', 'away']:
        for player in game_data[team]['players']:
            if player['name'] == player_name:
                return player
    
    return None

# player_name = "Jarrett Allen"
# print(player_stats(player_name))


def average_rebounds_by_shoe_brand():
    shoe_rebounds = {}
    
    for team in game_dict().values():
        for player in team['players']:
            shoe_brand = player['shoe_brand']
            rebounds = player['rebounds_per_game']
            
            if shoe_brand in shoe_rebounds:
                shoe_rebounds[shoe_brand].append(rebounds)
            else:
                shoe_rebounds[shoe_brand] = [rebounds]
    
    for brand, rebounds_list in shoe_rebounds.items():
        average_rebounds = sum(rebounds_list) / len(rebounds_list)
        print(f"{brand}: {average_rebounds:.2f}")

average_rebounds_by_shoe_brand()