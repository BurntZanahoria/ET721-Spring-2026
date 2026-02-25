"""
Justin Wu
Feb 24, 2026
Lab 8 - APIs
"""
# -----------------------------------
# Example 1: dataframe using Pandas
# -----------------------------------

import pandas as pd

# step 1: dict_ as the static template of an API
dict_ = {
    'a' : [11, 21, 31],
    'b' : [12, 22, 32]
}

# step 2: create a dataframe using pandas
df = pd.DataFrame(dict_)

# head method of the dataframe communicates with the API displaying the first few rows of the dataframe
print("\n Example 1: Simple API")
print(df.head())

# step 3: working with data in the dataframe
# mean method calculates and returns the mean value of df
print(f"The mean value is = \n{df.mean()}")

# -----------------------------------
# Example 2: Get NBA team from static.py file
# -----------------------------------
# step 1: data collection
from Static import get_teams

nba_teams = get_teams()

# testing
print(f"The first two teams: {nba_teams[:2]}")

# step 2: create dataframe
df_teams = pd.DataFrame(nba_teams)
print("\nAll Teams")
print(df_teams.head())

# step 3: working with the data in df_teams
df_warriors = df_teams[df_teams['nickname'] == 'Warriors']
print("\nWarriors")
print(df_warriors)

# -----------------------------------
# Example 3: working with external APIs
# -----------------------------------
# step 1: data collection
# download the pickle file
import requests 

url = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"

# save download file
file_name = "Golden_State.pkl"

print(f"\nDownloading external file!...")
response = requests.get(url)
if response.status_code == 200:
    with open(file_name, "wb") as f:
        f.write(response.content)
    print("Download complete!")
else:
    print("Download failed")

# step 2: create dataframe
#  b. load dataframe from a pickle file
games = pd.read_pickle(file_name)
print(f"\nGames from pickle file")
print(games.head())

# step 3: working with the data in the dataframe
#  c. filter GSW vs Raptors
warriors_vs_raptors = games[games['MATCHUP'].str.contains('TOR')]
# testing
print("\n GSW home games")
print(warriors_vs_raptors)

gsw_home_vs_raptors = warriors_vs_raptors[warriors_vs_raptors['MATCHUP'].str.contains('vs')]
gsw_away_vs_raptors = warriors_vs_raptors[warriors_vs_raptors['MATCHUP'].str.contains('@')]

# testing
print("\n GSW home games")
print(gsw_home_vs_raptors)

#  d. calculate the average of the home and away matches
home_avg_plus = gsw_home_vs_raptors['PLUS_MINUS'].mean()
away_avg_plus = gsw_away_vs_raptors['PLUS_MINUS'].mean()
home_avg_pts = gsw_home_vs_raptors['PTS'].mean()
away_avg_pts = gsw_away_vs_raptors['PTS'].mean()

print(f"GSW home average = {home_avg_plus}")
print(f"GSW away average = {away_avg_plus}")

#  e. visualization of data analysis
import matplotlib.pyplot as plt

metrics = ["PLUS_MINUS", "PTS"]
home_values = [home_avg_plus, home_avg_pts]
away_values = [away_avg_plus, away_avg_pts]

x = range(len(metrics))
bar_width = 0.35

plt.figure(figsize=(8,5))
plt.bar([i - bar_width/2 for i in x], home_values, width=bar_width, label = 'Home', color='skyblue')
plt.bar([i - bar_width/2 for i in x], away_values, width=bar_width, label = 'Away', color='orange')

plt.xticks(x, metrics)
plt.title("GSW vs Raptors")

plt.ylabel("Average value")
plt.legend()
plt.show(block=True)

input("Press Enter to close...")

# -----------------------------------
#Exercise – EPL CSV API
# -----------------------------------

print("\n EXERCISE")

# step 1: data collection (download CSV)
epl_url = "https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/en.1.csv"
file_name = "epl_matches.csv"

print("\nDownloading EPL data...")
response = requests.get(epl_url)
if response.status_code == 200:
    with open(file_name, "wb") as f:
        f.write(response.content)
    print("Download complete!")
else:
    print("Download failed!")
    # if download fails, stop here
    exit()

# step 2: load CSV into dataframe
df_epl = pd.read_csv(file_name)
print("\nEPL data preview:")
print(df_epl.head())

# step 3: working with the data
# 3c: filter home and away matches for a specific team, e.g., Liverpool
home_matches = df_epl[df_epl['HomeTeam'] == 'Liverpool']
away_matches = df_epl[df_epl['AwayTeam'] == 'Liverpool']

# 3d: calculate average goals scored at home and away
avg_home_goals = home_matches['FTHG'].mean()
avg_away_goals = away_matches['FTAG'].mean()

print(f"\nLiverpool average home goals = {avg_home_goals}")
print(f"Liverpool average away goals = {avg_away_goals}")

# 3e: visualization of data analysis
metrics = ["Goals Scored"]
home_values = [avg_home_goals]
away_values = [avg_away_goals]

x = range(len(metrics))
bar_width = 0.35

plt.figure(figsize=(6,4))
plt.bar([i - bar_width/2 for i in x], home_values, width=bar_width, label='Home', color='skyblue')
plt.bar([i + bar_width/2 for i in x], away_values, width=bar_width, label='Away', color='orange')
plt.xticks(x, metrics)
plt.title("Liverpool 2020-21 Season: Home vs Away Goals")
plt.ylabel("Average Goals")
plt.legend()
plt.show(block=True)

input("Press Enter to close...")