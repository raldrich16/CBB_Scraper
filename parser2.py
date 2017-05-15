import requests
from bs4 import BeautifulSoup
import re
import string


def get_team():
    team_name = input('Please enter team name (ex: "Arizona Wildcats"): ').replace(' ', '-').lower()
    return team_name


def get_team_page(team):
    team = team.replace(' ', '-').lower()
    r = requests.get('http://www.espn.com/mens-college-basketball/teams')
    c = r.content
    soup = BeautifulSoup(c, "lxml")
    team_url = soup.find('a', href=re.compile(team + '?'))
    return team_url['href']


def get_team_schedule(team):
    team_url = get_team_page(team)
    team_name = string.capwords(team_url.split("/")[-1].replace('-', ' '))
    team_id = team_url.split("/")[-2]
    r = requests.get("http://www.espn.com/mens-college-basketball/team/schedule/_/id/" + team_id)
    c = r.content
    soup = BeautifulSoup(c, "lxml")
    rows = soup.find_all("tr", {"class": re.compile('^oddrow|evenrow')})
    my_list = []
    for row in rows:
        # get date
        pattern = re.compile("^Sun|Mon|Tue|Wed|Thu|Fri|Sat")
        if not pattern.match(row.td.get_text()):
            continue
        date = row.td.get_text()
        # get opposing_team
        try:
            opposing_team = row.find("li", {"class": "team-name"}).a.get_text()
        except AttributeError:
            opposing_team = row.find("li", {"class": "team-name"}).get_text()
        # get result
        result = row.find("span", {"class": re.compile("redfont|greenfont")}).get_text()
        # get score
        score = row.find("li", {"class": "score"}).a.get_text()
        differential = score.split('-')
        stripped_scores = []
        for i in differential:
            i = ''.join(c for c in i if c.isdigit())
            stripped_scores.append(i)
        differential = list(map(int, stripped_scores))
        if result == 'W':
            differential = differential[0]-differential[1]
        else:
            differential = differential[1]-differential[0]
        my_list.append([date, opposing_team, result, score, differential])

    return team_name, my_list


def get_player_season_stats(team):
    team_url = get_team_page(team)
    team_name = string.capwords(team_url.split("/")[-1].replace('-', ' '))
    team_id = team_url.split("/")[-2]
    r = requests.get("http://www.espn.com/mens-college-basketball/team/stats/_/id/" + team_id)
    c = r.content
    soup = BeautifulSoup(c, "lxml")
    player_stats = soup.find_all("tr", {"class": re.compile("player")})
    player_season_stats = player_stats[-int(len(player_stats)/2):]
    season_stats = []
    for player in player_season_stats:
        for data in player:
            season_stats.append(data.get_text())
    i = 0
    final_season_stats = []
    while i < len(season_stats):
        final_season_stats.append(season_stats[i:i+16])
        i += 16
    return team_name, final_season_stats


def get_player_game_stats(team):
    team_url = get_team_page(team)
    team_name = string.capwords(team_url.split("/")[-1].replace('-', ' '))
    team_id = team_url.split("/")[-2]
    r = requests.get("http://www.espn.com/mens-college-basketball/team/stats/_/id/" + team_id)
    c = r.content
    soup = BeautifulSoup(c, "lxml")
    player_stats = soup.find_all("tr", {"class": re.compile("player")})
    player_game_stats = player_stats[:int(len(player_stats) / 2)]
    game_stats = []
    for player in player_game_stats:
        for data in player:
            game_stats.append(data.get_text())
    i = 0
    final_game_stats = []
    while i < len(game_stats):
        final_game_stats.append(game_stats[i:i + 12])
        i += 12
    return team_name, final_game_stats
