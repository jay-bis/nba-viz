
from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import commonplayerinfo

# headers needed for quick fix of bug on some async requests for
# nba_api (something is broken, don't know what)
headers = {
    'Host': 'stats.nba.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://stats.nba.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
}

# simple utility function to wrap nba_api player finder into easy, nice function
def getIds(fullName):
    # find player id by full name
    pd = players.find_players_by_full_name(fullName)
    player_id = pd[0]['id']

    # get the player's current team (seems quite extensive to do
    # it like this, but I don't want ppl to have to enter in
    # a team name as well just to get a shot chart)
    info = commonplayerinfo.CommonPlayerInfo(player_id, headers=headers)
    team_id = info.common_player_info.get_data_frame()['TEAM_ID'][0]
    # return id's as key-value pair
    return {'player_id': player_id, 'team_id': team_id}

def teamID(teamName):
    # find team ID by team name
   teamDict = teams.find_teams_by_full_name(teamName)
   if len(teamDict) == 0:
       teamDict = teams.find_teams_by_nickname(teamName)
   return teamDict[0]['id']