import streamlit as st
import json
import flag
from scoring import calculate_leaderboard
from utils import FLAGS

# Load data
with open("data/players.json") as f:
    players = json.load(f)

with open("data/teams.json") as f:
    teams = json.load(f)

with open("data/results.json") as f:
    results = json.load(f)

# Calculate leaderboard
leaderboard = calculate_leaderboard(players, teams, results)

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
    st.write(f"**{player}**: {score} pts")

# Results Section

st.subheader("📊 Results so far")

for result in results:
    home = result["home_team"]
    away = result["away_team"]
    hg = result["home_goals"]
    ag = result["away_goals"]

    st.write(f"⚽ **{home} {hg} - {ag} {away} **")

    # outcome
    if hg > ag:
        st.success(f"🔥 {home} win")
    elif ag > hg:
        st.success(f"🔥 {away} win")
    else:
        if result.get("penalties_winner"):
            winner = result["penalties_winner"]
            st.warning(f"🤝 Draw — 🏆 {FLAGS.get(winner, '')} {winner} win on pens")
        else:
            st.info("🤝 Draw")

    st.divider()