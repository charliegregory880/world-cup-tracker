import streamlit as st
import json
from scoring import calculate_leaderboard, SCORING
from datetime import datetime

# Load data
with open("data/players.json") as f:
    players = json.load(f)

with open("data/teams.json") as f:
    teams = json.load(f)

with open("data/results.json") as f:
    results = json.load(f)

with open("data/r32_teams.json") as f:
    r32_teams = json.load(f)

# Calculate leaderboard
leaderboard = calculate_leaderboard(players, teams, results)

# Mapping teams to players

team_to_player = {}

for player, teams_list in players.items():
    for team in teams_list:
        team_to_player[team] = player

# UI
st.title("🏆 World Cup Tracker")

st.subheader("Leaderboard")

# Sort and display
sorted_board = sorted(
    leaderboard.items(),
    key=lambda x: x[1],
    reverse=True
)

for player, score in sorted_board:
    st.markdown(f"**{player}**: {score} pts")

# Remaining Teams Section

st.subheader("Round of 32 — Player Teams")

cols = st.columns(4)
for i, (player, r32teams) in enumerate(r32_teams.items()):
    with cols[i % 4]:
        teams_html = "".join(f"<li>{r32team}</li>" for r32team in r32teams)
        st.markdown(
            f"""
            <div style="
                border: 1px solid #e0e0e0;
                border-radius: 10px;
                padding: 12px 16px;
                margin-bottom: 16px;
                background-color: #1e1e1e;
            ">
                <h4 style="margin: 0 0 8px 0; color: #ffffff;">{player}</h4>
                <ul style="margin: 0; padding-left: 18px; color: #cccccc;">
                    {teams_html}
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

# Results Section

st.subheader("📊 Results so far")

def get_points(team, goals_for, goals_against, result):
    tier = teams[team]["tier"]

    points = goals_for * SCORING[tier]["goal"]

    if goals_for > goals_against:
        points += SCORING[tier]["win"]

    elif goals_for == goals_against:
        if result.get("penalties_winner") == team:
            points += SCORING[tier]["win"]

    return points

for result in reversed(results):
    if None in (result["home_goals"], result["away_goals"]):
        continue
    
    home = result["home_team"]
    away = result["away_team"]
    hg = result["home_goals"]
    ag = result["away_goals"]

    st.markdown(f"⚽ **{home} {hg} - {ag} {away}**")

    # outcome
    if hg > ag:
        st.success(f"🔥 {home} win")
    elif ag > hg:
        st.success(f"🔥 {away} win")
    else:
        if result.get("penalties_winner"):
            winner = result["penalties_winner"]
            st.warning(f"🤝 Draw — 🏆 {winner} win on pens")
        else:
            st.info("🤝 Draw")

    # --- NEW: points per team + player ---
    home_points = get_points(home, hg, ag, result)
    away_points = get_points(away, ag, hg, result)

    st.write(
        f"{home} → {home_points} pts ({team_to_player[home]})  \n  "
        f"{away} → {away_points} pts ({team_to_player[away]})"
    )

    st.divider()

