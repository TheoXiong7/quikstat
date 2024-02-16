from nba_api.stats.endpoints import playercareerstats, playerdashptpass
from nba_api.stats.static import players, teams
import pandas as pd

def find_player(name):
    player = players.find_players_by_full_name(name)

    if player == []: return ['noname', 0]
    
    return [player[0]['full_name'], player[0]['id']]

def stats_career(pid):

	career = playercareerstats.PlayerCareerStats(player_id=pid)
	df = career.get_data_frames()[0]
	
	#tid = df['TEAM_ID'].tail(1)
	#passing = playerdashptpass.PlayerDashPtPass(player_id=pid, team_id=tid)
	#return passing.get_data_frames()[0]

	df = pd.concat([df.tail(3)])
	df = df.reset_index()
	df = df.drop(['index', 'PLAYER_ID', 'SEASON_ID', 'LEAGUE_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'PLAYER_AGE', 'GS', 'MIN'], axis=1)
	return df

def stats_season(pid):
    return 0

def stats_season_against(pid, tid):
    return 0

if __name__ == '__main__':
    print(stats_career(find_player("lebron")[1]))

