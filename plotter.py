from parser2 import get_team_schedule, get_player_season_stats, get_player_game_stats
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

class CbbStats:
    def __init__(self, team):
        self.team = team

    def team_schedule_dataframe(self):
        team_name, data = get_team_schedule(self.team)
        df = pd.DataFrame(data, columns=['DATE', 'OPPOSING_TEAM', 'RESULT', 'SCORE', 'DIFFERENTIAL']).set_index('DATE')
        return df

    def player_game_stats_dataframe(self):
        team_name, data = get_player_game_stats(self.team)
        df = pd.DataFrame(data, columns=['PLAYER', 'GP', 'MIN', 'PPG', 'RPG', 'APG', 'SPG', 'BPG', 'TPG', 'FG%', 'FT%',
                                         '3P%']).set_index('PLAYER')
        df[['GP', 'MIN', 'PPG', 'RPG', 'APG', 'SPG', 'BPG', 'TPG', 'FG%', 'FT%', '3P%']] = df[['GP', 'MIN', 'PPG',
            'RPG', 'APG', 'SPG', 'BPG', 'TPG', 'FG%', 'FT%','3P%']].apply(pd.to_numeric)
        return df

    def player_season_stats_dataframe(self):
        team_name, data = get_player_season_stats(self.team)
        df = pd.DataFrame(data, columns=['PLAYER', 'MIN', 'FGM', 'FGA', 'FTM', 'FTA', '3PM', '3PA', 'PTS', 'OFFR',
                                         'DEFR', 'REB', 'AST', 'TO', 'STL', 'BLK']).set_index('PLAYER')
        df[['MIN', 'FGM', 'FGA', 'FTM', 'FTA', '3PM', '3PA', 'PTS', 'OFFR','DEFR', 'REB', 'AST', 'TO', 'STL', 'BLK']]\
            = df[['MIN', 'FGM', 'FGA', 'FTM','FTA', '3PM', '3PA', 'PTS', 'OFFR', 'DEFR', 'REB', 'AST', 'TO', 'STL',
            'BLK']].apply(pd.to_numeric)

        return df

'''instance = CbbStats("Arizona Wildcats")
df = instance.player_game_stats_dataframe()
df.plot()
plt.show()'''

'''if __name__ == '__main__':

    instance = CbbStats(input("Please enter your team name: "))

    engine = create_engine('sqlite:///cbb.db')

    instance.player_game_stats_dataframe().to_sql("player_game_stats", engine, if_exists="replace")
    instance.player_season_stats_dataframe().to_sql("player_season_stats", engine, if_exists="replace")
    instance.team_schedule_dataframe().to_sql("team_results", engine, if_exists="replace")
    print("Created/updated cbb.db")'''




