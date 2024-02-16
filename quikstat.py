import stats 
import pandas as pd

player_id = 0
player_name = 'noname'

def predict(player):
    # calculate everything
    player_id = player[0]

    # weight stats
    # games against this team
    # last 5-game 
    # last 10 game
    # every 2 other games tracing back

    # weight opposing team defense
    # defense rating
    # rebounds
    # points allowed per area
    # player points scored in area
    # calculate predicted status

    # generate line
    # generate suggested o/u
    
    return 0

if __name__ == '__main__':
    print(stats.find_player('paul george'))