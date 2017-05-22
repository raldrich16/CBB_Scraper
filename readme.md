## CBB_Scraper
This program scrapes ESPN for college basketball data on a team input by the user.  It then creates three tables in cbb.db that track player
game stats, season stats, and team season stats.

## Code Sample
This function uses BeautifulSoup and requests to find a home page for the team argument provided on ESPN's college basketball site.
```
def get_team_page(team):
    team = team.replace(' ', '-').lower()
    r = requests.get('http://www.espn.com/mens-college-basketball/teams')
    c = r.content
    soup = BeautifulSoup(c, "lxml")
    team_url = soup.find('a', href=re.compile(team + '?'))
    return team_url['href']
```

## How to Use
Run the file plotter.py and the program will ask you to input a team name.  ESPN  uses the format "[school] + [team name]" so please use this
format (correct input ex: "Arizona Wildcats").  Do NOT use "University" at the beginning or end of the school name.  The SQLite database will then be placed in the root folder.

## Improvements and Expansion

* Account for imperfect input
* Allow for multiple teams to be inputted and then compared
* Add graphing functionality to look at player and team trends

## Contributors

Reed Aldrich
